import numpy as np
import tensorflow as tf
import gym
from tensorflow.keras import layers

# Define Actor and Critic networks
class Actor(tf.keras.Model):
    def __init__(self, action_dim, max_action):
        super(Actor, self).__init__()
        self.layer1 = layers.Dense(400, activation='relu')
        self.layer2 = layers.Dense(300, activation='relu')
        self.output_layer = layers.Dense(action_dim, activation='tanh')  # Output in the range [-1, 1] scaled by max_action

    def call(self, state):
        x = self.layer1(state)
        x = self.layer2(x)
        action = self.output_layer(x)
        return action * max_action

class Critic(tf.keras.Model):
    def __init__(self):
        super(Critic, self).__init__()
        self.layer1 = layers.Dense(400, activation='relu')
        self.layer2 = layers.Dense(300, activation='relu')
        self.output_layer = layers.Dense(1)

    def call(self, state, action):
        x = tf.concat([state, action], axis=-1)
        x = self.layer1(x)
        x = self.layer2(x)
        q_value = self.output_layer(x)
        return q_value

# Define DDPG Agent
class DDPGAgent:
    def __init__(self, state_dim, action_dim, max_action):
        self.actor = Actor(action_dim, max_action)
        self.actor_target = Actor(action_dim, max_action)
        self.critic = Critic()
        self.critic_target = Critic()

        # Define optimizers
        self.actor_optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        self.critic_optimizer = tf.keras.optimizers.Adam(learning_rate=0.002)

        # Other hyperparameters
        self.gamma = 0.99  # Discount factor
        self.tau = 0.005   # Soft update parameter

    def train_step(self, states, actions, rewards, next_states, dones):
        # Convert to tensors
        states = tf.convert_to_tensor(states, dtype=tf.float32)
        actions = tf.convert_to_tensor(actions, dtype=tf.float32)
        rewards = tf.convert_to_tensor(rewards, dtype=tf.float32)
        next_states = tf.convert_to_tensor(next_states, dtype=tf.float32)

        # Update critic
        with tf.GradientTape() as tape:
            target_actions = self.actor_target(next_states)
            target_q_values = self.critic_target(next_states, target_actions)
            target_values = rewards + self.gamma * target_q_values * (1 - dones)
            predicted_values = self.critic(states, actions)
            critic_loss = tf.keras.losses.MSE(target_values, predicted_values)
        critic_gradients = tape.gradient(critic_loss, self.critic.trainable_variables)
        self.critic_optimizer.apply_gradients(zip(critic_gradients, self.critic.trainable_variables))

        # Update actor
        with tf.GradientTape() as tape:
            actor_actions = self.actor(states)
            actor_loss = -tf.reduce_mean(self.critic(states, actor_actions))
        actor_gradients = tape.gradient(actor_loss, self.actor.trainable_variables)
        self.actor_optimizer.apply_gradients(zip(actor_gradients, self.actor.trainable_variables))

        # Soft update target networks
        self.soft_update_target_networks()

    def soft_update_target_networks(self):
        self.actor_target.set_weights([
            self.tau * w + (1 - self.tau) * w_target
            for w, w_target in zip(self.actor.get_weights(), self.actor_target.get_weights())
        ])
        self.critic_target.set_weights([
            self.tau * w + (1 - self.tau) * w_target
            for w, w_target in zip(self.critic.get_weights(), self.critic_target.get_weights())
        ])

# Training loop
env = gym.make('Pendulum-v1')  # Use the Pendulum environment

state_dim = env.observation_space.shape[0]
action_dim = env.action_space.shape[0]
max_action = env.action_space.high[0]

agent = DDPGAgent(state_dim, action_dim, max_action)

num_episodes = 100
max_steps = 200

for episode in range(num_episodes):
    state = env.reset()
    total_reward = 0

    for step in range(max_steps):
        # Choose action using the actor network
        state = np.expand_dims(state, axis=0)
        action = agent.actor(state).numpy()[0]

        # Take the action and observe the next state and reward
        next_state, reward, done, _ = env.step(action)

        # Train the agent
        agent.train_step(state, action, reward, next_state, done)

        state = next_state
        total_reward += reward

        if done:
            break

    print(f"Episode: {episode + 1}, Total Reward: {total_reward}")

# Save the trained model if needed
# agent.actor.save_weights('actor_weights.h5')
# agent.critic.save_weights('critic_weights.h5')
