from pylab import *
# http://www.pma.caltech.edu/Courses/ph136/yr2004/book03/chap07/0207.1.pdf

N = 1000
D = 3. # size of aperture
L = 20 # distance to screen
k = 6.  # wavenumber


def plot_cornu(N, size, distance, k):
    X = zeros(N)  # horizontal axis of our phasors
    Y = zeros(N)  # vertical axis of our phasors
    for i in range(-int(N/2), int(N/2)):
    #for i in range(N - 1):
        phase = pow(size * i, 2) / 2 / distance
        X[i+1] = X[i] + cos(phase)
        Y[i+1] = Y[i] + sin(phase)
    plot(X,Y)

for l in linspace(4,200,100):
    figure()
    plot_cornu(N, D, l, k)
    title('"sum over histories" at distance %dm\n size of aperture %d\n k %d'
            % (l, D, k))
    savefig("cornu%d.png" %(l))
#show()
