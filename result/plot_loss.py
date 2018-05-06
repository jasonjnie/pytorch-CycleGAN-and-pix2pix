#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
f = open('loss_log.txt')
epoch_iter = 1
epochInd = -1
epoch = []
all_G_A, all_Cyc_A, all_D_A, all_idt_A = [], [], [], []
all_G_B, all_Cyc_B, all_D_B, all_idt_B = [], [], [], []


for line in f:
    if line[:6] == '(epoch':
        line_split = line.split(' ')
        if int(line_split[1].split(',')[0]) != epochInd:
            #print(line_split)
            epochInd = int(line_split[1].split(',')[0])
            #losstemp = (float(line_split[11].split(',')[0]) + float(line_split[13].split(',')[0]) + float(line_split[17].split(',')[0])
            #            +float(line_split[19].split(',')[0]) + float(line_split[21].split(',')[0]) + float(line_split[23].split(',')[0]))
            G_A = float(line_split[11].split(',')[0])
            D_A = float(line_split[9].split(',')[0])
            Cyc_A = float(line_split[13].split(',')[0])
            #idt_A = float(line_split[21].split(',')[0])
            idt_A = 0
            G_B = float(line_split[17].split(',')[0])
            D_B = float(line_split[15].split(',')[0])
            Cyc_B = float(line_split[19].split(',')[0])
            #idt_B = float(line_split[23].split(',')[0])
            idt_B = 0

            epoch.append(epoch_iter)
            epoch_iter += 1
            all_G_A.append(G_A)
            all_Cyc_A.append(Cyc_A)
            all_D_A.append(D_A)
            all_idt_A.append(idt_A)
            all_G_B.append(G_B)
            all_Cyc_B.append(Cyc_B)
            all_D_B.append(D_B)
            all_idt_B.append(idt_B)
f.close()

fig1 = plt.figure(figsize=(9, 6))
plt.subplot(2,2,1)
plt.plot(epoch, all_G_A)
plt.title('generator loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.subplot(2,2,2)
plt.plot(epoch, all_D_A)
plt.title('discriminator loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.subplot(2,2,3)
plt.plot(epoch, all_Cyc_A)
plt.title('cycle-consistency loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.subplot(2,2,4)
plt.plot(epoch, all_idt_A)
plt.title('identity loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.tight_layout()
plt.suptitle('Class A (forward): Painting to Photo')
plt.savefig('A_loss.jpg')

fig2 = plt.figure(figsize=(9, 6))
plt.subplot(2,2,1)
plt.plot(epoch, all_G_B)
plt.title('generator loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.subplot(2,2,2)
plt.plot(epoch, all_D_B)
plt.title('discriminator loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.subplot(2,2,3)
plt.plot(epoch, all_Cyc_B)
plt.title('cycle-consistency loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.subplot(2,2,4)
plt.plot(epoch, all_idt_B)
plt.title('identity loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.tight_layout()
plt.suptitle('Class B (backward): Photo to Painting')
plt.savefig('B_loss.jpg')

