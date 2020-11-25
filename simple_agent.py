import time
import gym


def main():
    """Simple agent"""
    # initialize environment
    env = gym.make("Hopper-v2")
    env.reset()

    # start running agent
    done = False
    for i in range(1000):
        env.render()
        state, reward, done, info = env.step(env.action_space.sample())
        time.sleep(0.1)
    env.close()

    print("Done")


if __name__ == '__main__':
    main()