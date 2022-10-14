import rlgym
from rlgym.utils.reward_functions import RewardFunction
from rlgym.utils.gamestates import GameState, PlayerData
from rlgym_tools.extra_obs.advanced_stacker import AdvancedStacker
import numpy as np
import torch
import random
from GameBot.RL_bot.RainbowDQN.DQNAgent import DQNAgent


class MultiReward(RewardFunction):
    def reset(self, initial_state: GameState):
        pass

    def get_reward(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> float:
        goalreward = player.match_goals * 100
        savereward = player.match_saves * 45
        shotreward = player.match_shots * 10
        reward = goalreward + savereward + shotreward
        return reward

    def get_final_reward(self, player: PlayerData, state: GameState, previous_action: np.ndarray) -> float:
        return 0






if __name__ == "__main__":

    obs_builder = AdvancedStacker(stack_size=10)
    env = rlgym.make(obs_builder=obs_builder,
                     spawn_opponents=True,
                     self_play=False,
                     team_size=1,
                     reward_fn=MultiReward())

    # parameters
    num_frames = 20000
    memory_size = 10000
    batch_size = 128
    target_update = 100

    agent = DQNAgent(env, memory_size,batch_size,target_update,gamma=0.95)





