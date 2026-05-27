
from flask import Flask , render_template , request
import sqlite3
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('wasteproject.html')
@app.route('/get_waste',methods=["POST"])
def get_waste():
    city = request.form['city']
    conn=sqlite3.connect('wasteg_db.sqlite3')
    cursor=conn.cursor()
    cursor.execute("SELECT waste_type, weight from garbage where city=?", (city,))
    rows=cursor.fetchall()
    conn.close()
  
    greedy_result=sorted(rows,key=lambda x:x[1],reverse=True)
    highest_waste=greedy_result[0] if greedy_result else None
    frequency={}
    for row in rows:
        waste_type  =row[0]
        if waste_type in frequency:
            frequency[waste_type]+=1
        else:
            frequency[waste_type]=1
    most_frequent=max(frequency,key=frequency.get) if frequency  else None
    n=len(rows)
    dp=[0]*(n+1)
    for i in range(1,n+1):
        dp[i]=dp[i-1]+rows[i-1][1]
    total_waste=dp[n]
    return render_template(

        'wasteproject.html',

        selected_city=city,

        waste_data=rows,

        priority_waste=highest_waste,

        most_frequent=most_frequent,

        total_waste=total_waste
    )
if __name__=="__main__":
    app.run()