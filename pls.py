from sklearn.cross_decomposition import PLSRegression
pls1=PLSRegression(n_components=3)
y=[]
x=None
pre=None
with open("con", "r") as con, open("x_vals", "r") as x_vals, open("to_pred", "r") as to_pred:
    for lines in con:
        y.append(float(lines.strip()))
    for lines in x_vals:
        number_of_messurment= len(lines.split())
        if not x:
            x=[[]for i in range(number_of_messurment)]
        for i in range(number_of_messurment):
            x[i].append(float(lines.split()[i]))
    for lines in to_pred:
        number_of_messurment= len(lines.split())
        if not pre:
            pre=[[]for i in range(number_of_messurment)]
        for i in range(number_of_messurment):
            pre[i].append(float(lines.split()[i]))

pls1.fit(x,y)
predicted_con=pls1.predict(pre)
smaples=["jf","jp","pf","pp","sf","sp"]
sample_pred_dic={j:i.item() for i, j in zip(predicted_con, smaples)}

