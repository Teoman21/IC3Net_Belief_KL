import os

def main():
    target_file = '/Users/Teoman/Desktop/Classes/NU/Spring26/RL/project/IC3Net_Belief_KL/main.py'
    with open(target_file, 'r') as f:
        lines = f.readlines()
        
    out = []
    in_main = False
    for line in lines:
        if line.startswith('init_args_for_env(parser)'):
            in_main = True
            out.append("if __name__ == '__main__':\n")
            
        if in_main:
            if line.strip():
                out.append("    " + line)
            else:
                out.append("\n")
        else:
            out.append(line)
            
    with open(target_file, 'w') as f:
        for x in out:
            f.write(x)

if __name__ == '__main__':
    main()
