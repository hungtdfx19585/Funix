#thư viện
import pandas as pd
import numpy as np 

def mean(list_diem):
    return(sum(list_diem)/len(list_diem))

def median(list_diem):
    list_diem.sort()
    if(len(list_diem)%2==0):
        md1=(list_diem[len(list_diem)//2-1])
        md2=(list_diem[len(list_diem)//2])
        return ((md1+md2)/2)
    else:
        return(list_diem[len(list_diem)//2])

if __name__ == '__main__':
    filename = input("Enter a filename: ")
    #filename='class1'
    filediem=filename.split('.')[0]+'_grades.txt'
    if filename[-1:-4:-1]!='txt':
        filename=filename+'.txt'
    
    #try để tìm có file không
    try: 
        #Mở file
        with open(filename,'r') as filedoc:
            fd=filedoc.read()
        data=fd.split('\n')
        print('Successfully opened '+filename)
        
        #**** ANALYZING ****
        print('**** ANALYZING **** ')
        sodonghople=0
        list_diem=np.array([])
        for i in range(len(data)):
            diem=0
            sodong=data[i].split(',')
            if len(sodong)!= 26:
                print('Invalid line of data: does not contain exactly 26 values')
                print(data[i])
                continue
            
            elif (sodong[0][0]!='N' or 
                  len(sodong[0][1::])!=8 or 
                  not sodong[0][1::].isdigit()) :
                #Kiểm tra chữ đàu khác N hoặc sau N gồm 8 kí tự hoặc sau N không phải là số
                print('Invalid line of data: N# is invalid')
                print(data[i])      
                continue

            
            else:
                sodonghople+=1
                answer_key = np.array([
                    'B','A','D','D','C',
                    'B','D','A','C','C',
                    'D','B','A','B','A',
                    'C','B','D','A','C',
                    'A','A','B','D','D'])
                #Vòng lặp kiểm tra từng phần tử với kry
                for j in range(len(answer_key)):
                    if answer_key[j]==sodong[j+1]:
                        diem+=4
                    elif sodong[j+1]=='':
                        diem=diem
                    else:
                        diem-=1
                
                #Hàm DataFrame tạo 1 bảng,Hàm to_csv để lưu
                datadiemluu=pd.DataFrame({'ID':[sodong[0]],'Diem':[str(diem)]})
                datadiemluu.to_csv(
                    filediem,
                    header=False,
                    index=False,
                    mode='a')
            list_diem=np.append(list_diem,diem)
        if (sodonghople==len(data)):
            print('No errors found!')
        
        #**** REPORT ****
        list_diem.sort()
        print('**** REPORT ****')
        print('Total valid lines of data: ',sodonghople)
        print('Total invalid lines of data: ',(len(data)-sodonghople))
        print('Mean (average) score: ',round(mean(list_diem),2))
        print('Highest score: ',list_diem.max())
        print('Lowest score: ',list_diem.min())
        print('Range of scores: ',(list_diem.max()-list_diem.min()))
        print('Median score: ',median(list_diem))
    except:
        print("Sorry, I can't find this filename")
    