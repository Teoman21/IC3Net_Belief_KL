import sys
import gym
import ic3net_envs
from env_wrappers import *

def init(env_name, args, final_init=True):
    if env_name == 'levers':
        env = gym.make('Levers-v0', disable_env_checker=True).unwrapped
        env.multi_agent_init(args.total_agents, args.nagents)
        env = GymWrapper(env)
    elif env_name == 'number_pairs':
        env = gym.make('NumberPairs-v0', disable_env_checker=True).unwrapped
        m = args.max_message
        env.multi_agent_init(args.nagents, m)
        env = GymWrapper(env)
    elif env_name == 'predator_prey':
        env = gym.make('PredatorPrey-v0', disable_env_checker=True).unwrapped
        if args.display:
            env.init_curses()
        env.multi_agent_init(args)
        env = GymWrapper(env)
    elif env_name == 'traffic_junction':
        env = gym.make('TrafficJunction-v0', disable_env_checker=True).unwrapped
        if args.display:
            env.init_curses()
        env.multi_agent_init(args)
        env = GymWrapper(env)
    elif env_name == 'starcraft':
        env = gym.make('StarCraftWrapper-v0', disable_env_checker=True).unwrapped
        env.multi_agent_init(args, final_init)
        env = GymWrapper(env)

    elif env_name.startswith('simple_'):
        return init_mpe(env_name, args, final_init)
    else:
        raise RuntimeError("wrong env name")

    return env

def init_mpe(env_name, args, final_init=True):
    import multiagent.scenarios as scenarios
    from multiagent.environment import MultiAgentEnv
    scenario = scenarios.load(env_name + ".py").Scenario()
    world = scenario.make_world()
    env = MultiAgentEnv(world, scenario.reset_world, scenario.reward,
                        scenario.observation)
    env = MPEWrapper(env, args)
    args.num_actions = [env.num_actions]
    args.dim_actions = 1
    args.naction_heads = [env.num_actions]
    args.nfriendly = args.nagents
    return env

