"""Exam8: BishopMove

None shall pass ~
คุณได้เดินไปทั่วในหมู่บ้านชนบทนั้น ก็ได้ไปเจอกับโต๊ะพนันโต๊ะหนึ่ง ที่เล่นเกมกระดานหมากรุกสากล
ตัวคุณเองที่กำลังร้อนเงินอยู่นั้น จึงได้ตัดสินใจลงเล่นทันที

โดยที่จะพนันเพียงว่า เมื่อให้ตัว Bishop อยู่ในตำแหน่งใดๆบนกระดานแล้ว
Bishop ตัวนั้นจะสามารถเดินไปยังตำแหน่งที่ต้องการได้หรือไม่ ในการเดินเพียงครั้งเดียว
โดยที่มีหมากอีกหนึ่งตัวอยู่บนกระดานวางขวางไว้อยู่ ซึ่งอาจจะเป็นหมากฝั่งเดียวกับ Bishop (มิตร) หรือฝั่งตรงข้าม (ศัตรู) ก็ได้ แล้วแต่ที่กำหนดมา
ถ้าเส้นทางที่ Bishop ที่จะเดินไปยังเป้าหมายนั้น มีหมากอีกหนึ่งตัวขวางไว้อยู่ระหว่างทาง
Bishop จะไม่สามารถเดินไปได้ แต่ถ้าหากเป้าหมายที่จะเดินนั้นเป็นช่องเดียวกับหมากที่วางขวางไว้อยู่นั้น
ถ้าเป็นมิตรจะไม่สามารถเดินไปเป้าหมายได้ แต่ถ้าเป็นศัตรู จะสามารถเดินไปได้(กินหมากของฝ่ายศัตรูพอดี)
 
โดยที่กระดานหมากรุกสากลบนโต๊ะพนันนั้น จะมีขนาดเท่าใดก็ได้
หมาก Bishop กับหมากที่มีไว้วางขวาง จะไม่ได้อยู่ตำแหน่งเดียวกัน
และหมากทั้งสอง และเป้าหมายจะอยู่ตำแหน่งใดก็ได้ ภายในกระดาน
เนื่องจากกระดานอาจจะมีขนาดใหญ่มากจนดูยาก คุณจึงเขียนโปรแกรมขึ้นมาตรวจสอบ โดยที่รับข้อมูลกระดานลงไป และแสดงผลลัพธ์ออกมา
หากสามารถเดินไปยังเป้าหมายได้ ให้แสดงผลลัพธ์ว่า Yes
หากไม่สามารถเดินไปได้ ให้แสดงผลว่า No

[Tutorial กติกาหมากรุกสากล]
ตำแหน่งของกระดานจะเริ่มจาก (0, 0) ที่มุมซ้ายบน ไปจนถึง (6, 0) ที่มุมซ้ายล่าง
(0, 6) ที่มุมขวาบน และ (6, 6) ที่มุมขวาล่าง
**ในตัวอย่างแสดงกระดานขนาด 7 x 7

เกมกระดานหมากรุกสากลจะประกอบด้วยผู้เล่นสองฝั่ง ฝั่งดำ กับ ฝั่งขาว โดยที่คุณเป็นฝั่งสีขาว


ตัวหมาก Bishop นั้นจะเดินเป็นแนวทแยงมุม 4 ทิศได้เท่านั้น และระยะเท่าใดก็ได้ ดังแสดงด้วยลูกศรตามภาพ



ตำแหน่งเป้าหมายแสดงด้วยเครื่องหมายกากบาทดังภาพ
หาก Bishop วางตำแหน่งนี้ (5, 5) และเป้าหมายอยู่ในตำแหน่ง (1, 1)
Bishop จะสามารถเดินไปยังเป้าหมายได้ กรณีนี้ให้แสดงผลโปรแกรมว่า Yes 
(รูปนี้คือตัวอย่าง sample case 1 ด้านล่าง)



แต่ถ้าหากเป้าหมายอยู่นอกการเดินของ Bishop ดังกรณีนี้ (4, 1)
Bishop จะไม่สามารถเดินไปได้ ให้แสดงผลว่า No
(รูปนี้คือตัวอย่าง sample case 2 ด้านล่าง)



กรณีนี้ เป้าหมายอยู่ในทางเดินของ Bishop จริง
แต่มีหมากที่เป็นฝ่ายเดียวกันวางขวางอยู่ จึงไม่สามารถเดินไปยังเป้าหมายได้ กรณีนี้แสดงผลว่า No
(รูปนี้คือตัวอย่าง sample case 3 ด้านล่าง)



กรณีนี้หมากวางขวางเป็นศัตรูจริง แต่ว่าถ้าจะเดินไปเป้าหมายได้ ต้องกินหมากศัตรูก่อนหนึ่งตา
จึงไม่สามารถเดินไปยังเป้าหมายได้ภายในหนึ่งตาเดิน ให้แสดงผลว่า No
(รูปนี้คือตัวอย่าง sample case 4 ด้านล่าง)



กรณีนี้คล้ายกับกรณีที่แล้ว แต่ว่าเป้าหมายคือตำแหน่งเดียวกับหมากศัตรู
Bishop สามารถเดินไปกินหมากแล้วยืนอยู่ตำแหน่งเป้าหมายได้ทันที ให้แสดงผลว่า Yes
(รูปนี้คือตัวอย่าง sample case 5 ด้านล่าง)

จากรูปข้างบน ถ้าเปลี่ยนหมากศัตรูเป็นหมากฝ่ายเดียวกัน ก็ให้แสดงผลว่า No (เพราะเราเคลื่อนที่ไปทับหมากฝ่ายเดียวกันไม่ได้) 
 
by นายพิชาธร เอกอุ่น 
1 October 2016, 20:58
 Specification
 Input Specification	 Output Specification

9 บรรทัด
ขนาดกระดานในแนวของแถว (แนวนอน) { > 0 }
ขนาดกระดานในแนวของหลัก (แนวตั้ง) { > 0; ขนาดของกระดานจะมีพื้นที่รวมมากกว่าหนึ่งช่องเสมอ}
ตำแหน่งของ Bishop ในตำแหน่งแถว
ตำแหน่งของ Bishop ในตำแหน่งหลัก
ตำแหน่งของหมากที่วางขวางในตำแหน่งแถว
ตำแหน่งของหมากที่วางขวางในตำแหน่งหลัก
ตัวเลขระบุว่าเป็นศัตรูกับ Bishop หรือไม่ (0 ไม่ใช่, 1 ใช่)
ตำแหน่งเป้าหมายในตำแหน่งแถว
ตำแหน่งเป้าหมายในตำแหน่งหลัก 

บรรทัดเดียว
Yes หรือ No เท่านั้น

  
 Sample Case
 Sample Input	 Sample Output
7
7
5
5
6
6
1
1
1
Yes
7
7
5
5
6
6
1
4
1
No
7
7
2
4
4
2
0
5
5
No
10
15
2
4
4
2
1
5
5
No
8
8
2
4
4
2
1
4
2
Yes"""
def bishopmove():
    """1,2 0,1 2,3 0,3 2,1 3,0"""
    row, col = int(input()), int(input())
    row, col = col, row
    qx1 = int(input())
    qy1 = int(input())
    bx1 = int(input())
    by1 = int(input())
    bo1 = int(input())
    tx1 = int(input())
    ty1 = int(input())
    if qx1-qy1 == tx1-ty1 or qy1-tx1 == ty1-qx1:
        if bx1 == tx1 and by1 == ty1:
            if bo1:
                return "Yes"
            return "No"
        if bx1 in [range(min(qx1, tx1), max(qx1, tx1))] \
           and by1 in list(range(min(qy1, ty1), max(qy1, ty1))):
            return "No"
        return "Yes"
    return "No"
print(bishopmove())
