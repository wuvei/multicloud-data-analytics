import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # up = 510*1024
    # x = np.linspace(0, up, up * 10)
    # aws0 = [1 if (i <= 1) else 0 for i in x]
    # aws1 = [1 if ((i > 1) and (i <= 10240)) else 0 for i in x]
    # aws2 = [1 if ((i > 10240) and (i <= 50*1024)) else 0 for i in x]
    # aws3 = [1 if ((i > 50*1024) and (i <= 150*1024)) else 0 for i in x]
    # aws4 = [1 if ((i > 150*1024)) else 0 for i in x]
    

    # aws_price = 0*x*aws0 + (x-1)*0.09*aws1 + ((10240-1)*0.09 + (x - 10240)*0.085)*aws2 + ((10240-1)*0.09 + 40*1024*0.085 + (x - 50*1024)*0.07)*aws3 + ((10240-1)*0.09 + 40*1024*0.085 + 100*1024*0.07 + (x - 150*1024)*0.05)*aws4

    # aws_price = 0*x*aws0 + (x-1)*0.09*aws1 + ((10240-1)*0.09 + (x - 10240)*0.085)*aws2 + ((10240-1)*0.09 + 40*1024*0.085 + (x - 50*1024)*0.07)*aws3

    # azure0 = [1 if (i <= 5) else 0 for i in x]
    # azure1 = [1 if ((i > 5) and (i <= 10240)) else 0 for i in x]
    # azure2 = [1 if ((i > 10240) and (i <= 50*1024)) else 0 for i in x]
    # azure3 = [1 if ((i > 50*1024) and (i <= 150*1024)) else 0 for i in x]
    # azure4 = [1 if ((i > 150*1024)) else 0 for i in x]

    # azure_price = 0*x*azure0 + (x-5)*0.087*azure1 + ((10240-5)*0.087 + (x - 10240)*0.083)*azure2 + ((10240-5)*0.09 + 40*1024*0.083 + (x - 50*1024)*0.07)*azure3 + ((10240-5)*0.09 + 40*1024*0.083 + 100*1024*0.07 + (x - 150*1024)*0.05)*azure4
    # plt.plot(x/1024, aws_price, color="red", label="aws: US East(N. Virginia)")
    # plt.plot(x/1024, azure_price, color="blue", label="azure: East US")

    x_label = ["0GB", "1GB", "5GB", "10TB", "50TB", "150TB", "500TB"]
    x = [0, 1, 3, 6, 12, 20, 30]
    
    aws_price = [0, 0, 0.5, 1.5, 4, 8, 16]
    aws_price = [0, 0,    2,      6,      10,       15,       20]
    aws_label = [0, 0, 0.36, 921.51, 4403.11, 11571.11, 29491.11]
    
    azure_price = [0, 0, 0, 5, 9, 14, 19]
    azure_label = [0, 0, 0, 890.44, 4290.13, 11458.13, 29378.13]
    
    google_low_price = [0, 1, 3, 4, 8, 13, 18]
    google_stand = [0, 0.09, 0.43, 870.73, 3532.80, 10188.80, 26316.80]
    
    google_prem_price = [0, 1.2, 3.3, 7, 12, 17, 23]
    google_prem_price = [0, 1.7, 4, 7, 12, 17, 23]
    google_prem = [0, 0.72, 3.63, 7424.0, 30771.20, 88627.20, 274995.20]
    google_prem[:] = [x / 5 for x in google_prem]

    plt.plot(x, aws_price, color="red", label="aws: US East(N. Virginia)")
    plt.plot(x, azure_price, color="blue", label="azure: East US")
    plt.plot(x, google_low_price, color="green", label="GC: North Virginia Standard Tier")
    plt.plot(x, google_prem_price, color="black", label="GC: North Virginia Premier Tier Average")

    for x1, y1, l in zip(x, aws_price, aws_label):
        plt.text(x1, y1, l, ha="center", va="bottom", fontsize=8)
    for x1, y1, l in zip(x, azure_price, azure_label):
        plt.text(x1, y1, l, ha="center", va="bottom", fontsize=8)
    for x1, y1, l in zip(x, google_low_price, google_stand):
        plt.text(x1, y1, l, ha="center", va="bottom", fontsize=8)
    for x1, y1, l in zip(x, google_prem_price, google_prem):
        plt.text(x1, y1, l, ha="center", va="bottom", fontsize=8)

    plt.legend()
    plt.xticks(x, x_label, rotation = 20)
    plt.yticks([])
    # plt.yscale('log')
    # plt.xscale('log')
    plt.show()