"""
2.6(p.57)
問題2-3
投射軌跡比較プログラムを拡張する
* 飛行時間，最大水平距離，最大垂直距離を投射の速度と角度の各組について出力
* 投射の速度と角度の値をユーザからいくつでも受け取れるプログラムにする

projectile_comparison_gen.py

Compare the projectile motion of a body thrown with various combinations of initial 
velocity and angle of projection.
"""

import matplotlib.pyplot as plt
import math

# 2.4.2.2(p.53) Draw the trajectory of a body in projectile motion とgの書く位置が違う
g = 9.8

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion at different initial velocities and angles')

"""
2.4.2.1(p.53)
Generate equally spaced floating point
numbers between two given values
2つの値の間の等間隔な浮動小数点数の生成
"""
def frange(start, final, interval):

    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    
    return numbers

def draw_trajectory(u, theta, t_flight):
    # list of x and y co-ordinates
    x = []
    y = []
    intervals = frange(0, t_flight, 0.001)
    for t in intervals:
        x.append(u*math.cos(theta)*t) # 水平距離(S_x) cf.p.51
        y.append(u*math.sin(theta)*t - 0.5*g*t*t) # 垂直距離(S_y) df.p.52

    # create the graph
    draw_graph(x, y)

if __name__ == '__main__':
"""
cf.p.59 try...except ブロックを使うように言われている
"""
    try:
        num_trajectories = int(input('How many trajectories? ')) # 何回値を受け取るか
    
        velocities = []
        angles = []
        for i in range(1, num_trajectories+1):
            v = input('Enter the initial velocity for trajectory {0} (m/s): '.format(i)) # 速度
            theta = input('Enter the angle of projection for trajectory {0} (degrees): '.format(i)) # 角度
            velocities.append(float(v))
            angles.append(math.radians(float(theta)))

        for i in range(num_trajectories):
            # calculate time of flight, maximum horizontal distance and
            # maximum vertical distance
            t_flight = 2*velocities[i]*math.sin(angles[i])/g # Time of flight cf.p.52
            S_x = velocities[i]*math.cos(angles[i])*t_flight
            S_y = velocities[i]*math.sin(angles[i])*(t_flight/2) - (1/2)*g*(t_flight/2)**2
            print('Initial velocity: {0} Angle of Projection: {1}'.format(velocities[i], math.degrees(angles[i])))
            print('T: {0} S_x: {1} S_y: {2}'.format(t_flight, S_x, S_y))
            print()
            draw_trajectory(velocities[i], angles[i], t_flight)
        
        # Add a legend (凡例) and show the graph
        legends = []
        for i in range(0, num_trajectories):
            legends.append('{0} - {1}'.format(velocities[i], math.degrees(angles[i])))
        plt.legend(legends)
    except ValueError:
        print('You entered an invalid input')
    else:
        plt.show()