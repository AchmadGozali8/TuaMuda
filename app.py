from flask import Flask, redirect,request,render_template
app = Flask(__name__)

data = {
	
	'user':{
		'namaUser':[],
		'pilihanUser':{
			'muda':[],
			'tua':[]
		}
	},
	'object':{
		'namaObject':'Nur Rahmawati',
		'umurObject':23
	}
}

@app.route('/choose')
def index():
	return render_template('index.html')


@app.route('/login',methods=["GET","POST"])
def user():
	return render_template('login.html')

	nama = request.form['nama']
	if request.method=='POST':
		if nama == "":
			error()
		else:
			data['user']['namaUser']=nama
			return redirect(url_for('choose'))

@app.route('/pilihan')
def main():	
	tua = request.form.get('tua',None)
	muda = request.form.get('muda',None)
	
	if tua == 'tua':
		data['user']['pilihanUser']['tua']= 'tua'
	else:
		data['user']['pilihanUser']['muda']= 'muda'

def result():
#menampilkan hasil jika kondisi sesuai
	print "Result"
	jumlahUser=len(data['user']['namaUser'])
	muda = len(data['user']['pilihanUser']['muda'])
	tua = len(data['user']['pilihanUser']['tua'])
	if jumlahUser == 10:
		print "Yang menganggap anda muda",muda,"orang"
		print "Yang menganggap anda tua",tua,"orang"
		print "Umur asli object ",data['object']['umurObject']

if __name__ == "__main__":  
    app.run(host='0.0.0.0', port=9001, debug=True)
