from tkinter import *
import controller 
from multiprocessing import Process



def start():

#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     pass
    
    


    controller.startController()
    # controller.startListener()

# def create():
window = Tk()
window.title("Window")
window.geometry("200x200")
window.configure(bg = "white")
startBtn = Button(text = "ON", command = start, activeforeground = "green", width = 20, height = 3, justify=CENTER)
startBtn.place(relx=0.5, rely=0.2, anchor=CENTER)
window.mainloop()

# if __name__=='__main__':
    # t1 = Process(target=controller.startController)
    # t2 = Process(target=controller.startListener)
    # t3 = Process(target=create())
    # t3.start()

    # for t in threads:
    #     t.join()
     













