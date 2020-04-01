from flask import Flask , request
import json


@app.route('/classificar' , methods=['POST' , 'GET'])
def classificar():
	dados = request.get_json()
	idade = dados['idade']
	comorbidade = dados['comorbidade']
	contatoSuspeito = dados['contatoSuspeito']
	temperatura = dados['temperatura']
	pulso = dados['pulso']
	respiracao = dados['respiracao']
	tosseSeca = dados['tosseSeca']
	diarreia = dados['diarreia']
	fApetite = dados['fApetite']
	odores = dados['odores']
	sabores = dados['sabores']
	dorGarganta = dados['dorGarganta']
	dorCorpo = dados['dorCorpo']
	nariz = dados['nariz']
	fadiga = dados['fadiga']
	nausea = dados['nausea']
	febre = 0
	idoso = 0
	sangue = 0
	pulmao = 0

	if idade > 50:
		idoso = 1


	if temperatura > 37:
		febre = 1
	
	if pulso < 60:
		sangue = 1

	if respiracao > 20:
		pulmao = 1
	
	if (contatoSuspeito == 0) and (comorbidade == 0):
		if (febre == 0) and ((tosseSeca == 0) or (nariz == 0) or (dorGarganta == 0) or (pulmao == 0)):
			return { 'situacao' : 'Situaçao 1'}
		else:
			if idoso == 1 :
				return { 'situacao' : 'Situaçao 4'}
			else:
				return { 'situacao' : 'Situaçao 2'}

	else:
		if (febre == 0) and ((tosseSeca == 0) or (nariz == 0) or (dorGarganta == 0) or (pulmao == 0)):
			if idoso == 1:
				return {'situacao' : 'Situação 5'}

			else:
				return {'situacao' : 'Situação 3'}


if __name__ == '__main__' :
	app.run(debug=True)



	# Vetor Pessoa que futuramente vamos comparar para fazer a distancia euclidiana em relacao ao caso de COVID
	# pessoa = [ idade , comorbidade , contatoSuspeito , temperatura , pulso , respiracao , tosseSeca , diarreia , fApetite , odores , sabores , dorGarganta , dorCorpo , nariz , fadiga , nausea ]

	'''vteste = [ febre , sangue , pulmao ,tosseSeca ,diarreia , fApetite , odores , sabores , dorGarganta , dorCorpo , nariz ,fadiga , nausea]

	vCOVID = [1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1]

	vGRIPE = [1 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 0 , 0]

	vALERG = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0]

	vNORMAL = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]

	'''

