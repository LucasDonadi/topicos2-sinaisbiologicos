import numpy as np

import matplotlib.pyplot as plt
from matplotlib import rcParams, cm

def main():
    
    ####### LOAD DATASET #######
    num_subjects = 10 # quantidade de pessoas
    num_classes = 3 # quantidade de movimento
    num_trials = 8 # quantidade de repetições
    num_channels = 4 # quantidade de canais/eletrodos
    num_samples = 1600 # quantidade de amostras

    all_data = np.empty((num_subjects, num_classes, num_trials, num_channels, num_samples))
    data = np.empty((num_classes, num_trials, num_channels, num_samples))
    global_data = np.empty((num_subjects * num_classes, num_trials, num_channels, num_samples))

    # Carregar os dados para cada pessoa
    for subject_id in range(1, num_subjects + 1):
        
        # Carregar os dados dos três movimentos
        for class_id in range(1, num_classes + 1):
            file_path = f'./sEMG/datasets/topicos_cc/s{subject_id:02d}_{class_id}.npy'
            
            loaded_data = np.load(file_path) # shape (8,1600,4)
            loaded_data = np.moveaxis(loaded_data, 1, -1)  # shape (8,4,1600)

            data[class_id - 1, :, :, :] = loaded_data
            all_data[subject_id-1, class_id-1, :, :, :] = loaded_data
            
            start_index = (subject_id - 1) * num_classes + (class_id - 1)
            end_index = start_index + 1
            
            global_data[start_index:end_index, :, :, :] = loaded_data
                        
    print(f'{data.shape} - (classes, ensaios, canais, linhas)')
    print(f'{all_data.shape} - (voluntarios, classes, ensaios, canais, linhas)')
    print(f'{global_data.shape} - (voluntarios, ensaios, canais, linhas)')
    
    ###### VISUALIZAÇÃO DOS DADOS #####
    
    # [classe 1, ensaio 1, canal 1], [classe 1, ensaio 1, canal 2]
    # d1 = data[0,0,0,:], data[0,0,1,:], data[0,0,2,:], data[0,0,3,:]
    
    # # [classe 1, ensaio 2, canal 1], [classe 1, ensaio 2, canal 2]
    # d2 = data[0,1,0,:], data[0,1,1,:], data[0,1,2,:], data[0,1,3,:]

    # rcParams['figure.figsize'] = [16., 10.]

    # x = np.linspace(0, 5, num_samples)
    # fig, ax = plt.subplots(2, 1)

    # ax[0].plot(x, d1[0])
    # ax[0].plot(x, d1[1])
    # ax[0].plot(x, d1[2])
    # ax[0].plot(x, d1[3])

    # ax[1].plot(x, d2[0])
    # ax[1].plot(x, d2[1])
    # ax[1].plot(x, d2[2])
    # ax[1].plot(x, d2[3])

    # plt.show()
    
    ###### VISUALIZAÇÃO DOS DADOS DO LUCAS ######
    
    # d1 = all_data[6,0,0,0,:], all_data[6,0,0,1,:], all_data[6,0,0,2,:], all_data[6,0,0,3,:]
    
    # # [classe 1, ensaio 2, canal 1], [classe 1, ensaio 2, canal 2]
    # d2 = all_data[6,0,1,0,:], all_data[6,0,1,1,:], all_data[6,0,1,2,:], all_data[6,0,1,3,:]

    # rcParams['figure.figsize'] = [16., 10.]

    # x = np.linspace(0, 5, num_samples)
    # fig, ax = plt.subplots(2, 1)

    # ax[0].plot(x, d1[0])
    # ax[0].plot(x, d1[1])
    # ax[0].plot(x, d1[2])
    # ax[0].plot(x, d1[3])

    # ax[1].plot(x, d2[0])
    # ax[1].plot(x, d2[1])
    # ax[1].plot(x, d2[2])
    # ax[1].plot(x, d2[3])

    # plt.show()
    
    ##### VISUALIZAÇÃO EM 3D DOS DADOS DO LUCAS ######
    
    rcParams['figure.figsize'] = [18., 6.]

    for trial in (0, 1):
        mov = 1
        plot_data = []
        for channel in range(2):
            for i, t in enumerate(np.linspace(0, 1, 4000)):
                if i < num_samples:  # Verificar se o índice está dentro dos limites
                    plot_data.append([channel, t, all_data[6][mov][trial][channel][i]])

    plot_data = np.array(plot_data)
    x, y, z = plot_data[:,0], plot_data[:,1], plot_data[:,2]
    ax = plt.axes(projection ='3d')
    ax.set_title('Movimento {}'.format(mov + 1))
    ax.set_xlabel('Canais')
    ax.set_ylabel('Tempo (s)')
    ax.set_zlabel('Potência (mV)')
    ax.plot_trisurf(x, y, z, antialiased=True, cmap=cm.inferno, linewidth=1)
    plt.show()
    
    # rcParams['figure.figsize'] = [18., 6.]

    # for trial in (0, 1):
    #     mov = 1
    #     plot_data = []
    #     for channel in range(2):
    #         for i, t in enumerate(np.linspace(0, 1, 4000)):
    #             if i < num_samples:  # Verificar se o índice está dentro dos limites
    #                 plot_data.append([channel, t, global_data[mov][trial][channel][i]])

    # plot_data = np.array(plot_data)
    # x, y, z = plot_data[:,0], plot_data[:,1], plot_data[:,2]
    # ax = plt.axes(projection ='3d')
    # ax.set_title('Movimento {}'.format(mov + 1))
    # ax.set_xlabel('Canais')
    # ax.set_ylabel('Tempo (s)')
    # ax.set_zlabel('Potência (mV)')
    # ax.plot_trisurf(x, y, z, antialiased=True, cmap=cm.inferno, linewidth=1)
    # plt.show()
    
if __name__ == "__main__":
    main()

