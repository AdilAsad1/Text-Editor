import sys
import pickle
class Cursor():
    def __init__(self):
        self.CursorLocRow = 0
        self.CursorLocCol = 0
        self.CurrentRow = None
        self.CurrentCol = None

    def goto(self,indexrow,indexcol):
        if indexcol == 1:
            C.CurrentCol = CList.headSentinal.next
            C.CursorLocCol = 0
        else:
            C.CurrentCol = CList.headSentinal
            C.CursorLocCol = -1
        if CList.nodecount > indexcol:
            if indexcol == 1:
                for i in range(indexcol):
                    C.CurrentCol = C.CurrentCol.next
                    C.CursorLocCol += 1
            else:   
                for i in range(indexcol + 1):
                    C.CurrentCol = C.CurrentCol.next
                    C.CursorLocCol += 1
        else:
            while CList.nodecount - 1 != indexcol:
                RList = DLinkedList()
                RList.InsertRow(' ')
                CList.AddLast(RList.headSentinal)
                CList.RowLis.append(RList)
                C.CurrentCol = C.CurrentCol.next
                C.CursorLocCol += 1
            if indexcol != 1:
                C.CurrentCol = C.CurrentCol.next
                C.CursorLocCol += 1

        C.CurrentRow = CList.RowLis[indexcol].headSentinal.next
        C.CursorLocRow = 0
        if CList.RowLis[indexcol].nodecount  > indexrow:
            for i in range(indexrow):
                C.CurrentRow = C.CurrentRow.next
                C.CursorLocRow += 1

        else:
            while CList.RowLis[indexcol].nodecount -1 != indexrow:
                CList.RowLis[indexcol].AddLast(' ')
                C.CurrentRow = C.CurrentRow.next
                C.CursorLocRow += 1
        



    def Forward(self):
        if C.CurrentRow.next.next != None:
            C.CurrentRow = C.CurrentRow.next
            C.CursorLocRow += 1
        elif C.CurrentRow.next.next == None and C.CurrentCol.next.next == None:
            return
        else:
            C.CurrentCol = C.CurrentCol.next
            C.CursorLocCol += 1
            C.CurrentRow = CList.RowLis[C.CursorLocCol].headSentinal.next
            C.CursorLocRow = 0

    def Back(self):
        if C.CurrentRow.prev.prev != None:
            C.CurrentRow = C.CurrentRow.prev
            C.CursorLocRow -= 1

        elif C.CursorLocRow == 0 and C.CursorLocCol == 0:
            return
        
        else:
            C.CurrentCol = C.CurrentCol.prev
            C.CursorLocCol -= 1
            C.CurrentRow = CList.RowLis[C.CursorLocCol].tailSentinal.prev
            C.CursorLocRow = CList.RowLis[C.CursorLocCol].nodecount
        
        

            
                
class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLinkedList(Cursor):
    def __init__(self):
        self.headSentinal = Node(None)
        self.tailSentinal = Node(None)
        self.headSentinal.next = self.tailSentinal
        self.tailSentinal.prev = self.headSentinal
        self.nodecount = 0
        self.RowLis = []


    def InsertRow(self, string):
        for i in string:
            n = Node(i)
            self.tailSentinal.prev.next = n
            n.prev = self.tailSentinal.prev
            self.tailSentinal.prev = n
            n.next = self.tailSentinal
            self.nodecount += 1

    def InsertAfter(self,data):
        data = data[::-1]
        for i in data:
            n = Node(i)
            n.next = C.CurrentRow.next
            C.CurrentRow.next = n
            n.prev = C.CurrentRow
            n.next.prev = n
            self.nodecount += 1
        


    def AddLast(self, data):
        n = Node(data)
        self.tailSentinal.prev.next = n
        n.prev = self.tailSentinal.prev
        self.tailSentinal.prev = n
        n.next = self.tailSentinal
        self.nodecount += 1


    def Print(self):
        n = self.headSentinal.next
        while n.next != None:
            t = n.data.next
            while t.next != None:
                if n == C.CurrentCol and t == C.CurrentRow:
                    print('|',end ='')
                print(t.data, end ='')
                t = t.next
            n = n.next
            print('\n')


    def Delete(self, p):
        C.CurrentRow = C.CurrentRow.next
        p.prev.next = p.next
        p.next.prev = p.prev
        self.nodecount -= 1

def Save(obj,filename):
    with open(filename,'wb') as output:
        pickle.dump(obj,output)
    print('File Saved')

def Load(filename):
    with open(filename,'rb') as input:
        t = pickle.load(input)
    print('File Loaded')


        
C = Cursor()
CList = DLinkedList()

def main():
    RList = DLinkedList()
    RList.InsertRow(' ')
    global CList
    CList.AddLast(RList.headSentinal)
    CList.RowLis.append(RList)
    C.CurrentCol = CList.headSentinal.next
    C.CurrentRow = CList.RowLis[0].headSentinal.next
    
    


    while True:
        inStr = input('>> ')
        inStr = inStr.lower()

        if 'insert' in inStr:
            inStr = inStr.split(' ',1)
            if len(inStr) < 2:
                print('Invalid Command')
            else:
                rowlis = CList.RowLis[C.CursorLocCol]
                rowlis.InsertAfter(inStr[1])
            

        if inStr == 'print' or inStr == 'Print' or inStr == 'PRINT':
            CList.Print()


        if inStr == 'quit' or inStr == 'Quit' or inStr == 'QUIT':
            sys.exit(0)

        if 'goto' in inStr:
            gotoStr = inStr.split()
            if len(gotoStr) != 3:
                print('Invalid Command')
                
            else:
                indexrow = int(gotoStr[1])
                indexcol = int(gotoStr[2])
                C.goto(indexrow,indexcol)


        if 'delete' in inStr:
            delStr = inStr.split()
            if len(delStr) != 2:
                print('Invalid Command')
            else:
                
                for i in range(int(delStr[1])):
                    currow = C.CurrentRow
                    CList.RowLis[C.CursorLocCol].Delete(currow)

        if inStr == 'countlines' or inStr == 'Countlines' or inStr == 'COUNTLINES':
            print(CList.nodecount)

        if inStr == 'countcharacters' or inStr == 'Countcharacters' or inStr == 'COUNTCHARACTERS':
            count = 0
            for i in CList.RowLis:
                count = count + i.nodecount

            print(count)

        if inStr == 'forward' or inStr == 'Forward' or inStr == 'FORWARD':
            C.Forward()

        if inStr == 'back' or inStr == 'Back' or inStr == 'BACK':
            C.Back()

        if inStr == 'save' or inStr == 'Save' or inStr == 'SAVE':
            file = input('Enter filename: ')
            Save(CList,file)

        if inStr == 'load' or inStr == 'Load' or inStr == 'LOAD':
            loadfile = input('Enter filename: ')
            Load(loadfile)
            

        elif 'insert' not in inStr and inStr != 'load' and inStr != 'save' and inStr != 'back' and inStr != 'forward' and inStr != 'countcharacters' and inStr != 'countlines' and 'delete' not in inStr and 'goto' not in inStr and inStr != 'quit' and inStr != 'print':
            print('Invalid Command')
                    
            
            



main()

     
