#!/usr/bin/python
from Tkinter import *
import ttk
import pyaudio
import wave
import time
import sys
import tkFileDialog
import os
import struct
pause=0
one_prog=0
wf = wave.open('3.wav', 'rb')
p = pyaudio.PyAudio()
pflag=1
print "done"
inp_file1=''
r1=[]
type_channel1 = wf.getnchannels()
sample_rate1 =wf.getframerate()
sample_width1 = wf.getsampwidth()
num_frames1 = wf.getnframes()
inp_file2=''
r2=[]
type_channel2 = wf.getnchannels()
sample_rate2 =wf.getframerate()
sample_width2 = wf.getsampwidth()
num_frames2 = wf.getnframes()
inp_file3=''
r3=[]
type_channel3 = wf.getnchannels()
sample_rate3 =wf.getframerate()
sample_width3 = wf.getsampwidth()
num_frames3 = wf.getnframes()

type_channel = wf.getnchannels()
sample_rate =wf.getframerate()
sample_width = wf.getsampwidth()
num_frames = wf.getnframes()

def callback2(in_data, frame_count, time_info, status):
	data = wf.readframes(frame_count)
	return (data, pyaudio.paContinue)
	
def callback(in_data, frame_count, time_info, status):
	data = wf.readframes(frame_count)
	global pause
	if pause==0:
		return (data, pyaudio.paContinue)
	else:
		return (data, pyaudio.paAbort)
def prep(inp,filen):
	global r1
	global pause
	global r2
	global r3
	if inp==0:
		pause=1
	else:
		pause=0
	if pause==0:
		if inp==1:
			r1=readFile(1,filen)
			print scale13.get()
			print "shift below"
			print scale12.get()
			amplify(1)
			reversal(rev1,1)
			time_shift(scale12,1)
			tscale(scale13,1)
			save(1)
			play('ampli1.wav')
		elif inp==2:
			r2=readFile(2,filen)
			#print r1
			amplify(2)
			reversal(rev2,2)
			time_shift(scale22,2)
			tscale(scale23,2)
			save(2)
			play('ampli2.wav')
		elif inp==3:
			r3=readFile(3,filen)
			#print r1
			amplify(3)
			reversal(rev3,3)
			time_shift(scale12,3)
			tscale(scale33,3)
			save(3)
			play('ampli3.wav')
	else:
		pause=1	
def play(out_file):
	global pflag
	print pflag
	global wf
	global p
	wf = wave.open(out_file, 'rb')
	p = pyaudio.PyAudio()
	
	print "amplified the file and now playing the out file"
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True,
		stream_callback=callback)
	
	stream.start_stream()
	root.mainloop()
	
	stream.stop_stream()
	pflag=0
	stream.close()
	p.terminate()
def play1(out_file):
	global wf
	global p
	wf = wave.open(out_file, 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True,
		stream_callback=callback2)
	
	stream.start_stream()
	root.mainloop()
	
	stream.stop_stream()
	pflag=0
	stream.close()
	p.terminate()
def play2(out_file):
	global wf
	global p
	wf = wave.open(out_file, 'rb')
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True,
		stream_callback=callback2)
	
	stream.start_stream()
	root.mainloop()
	
	stream.stop_stream()
	pflag=0
	stream.close()
	p.terminate()
def open_file(typer):
	print "opening file*"
	global inp_file1
	global inp_file2
	global inp_file3
        ftypes = [('Wave files', '*.wav'), ('All files', '*')]
        dlg = tkFileDialog.Open(root, filetypes = ftypes)
        fl = dlg.show()
	#ias = fl.split('/')
	#ilen = len(ias)
	if typer ==1:
		inp_file1 = fl
		flabel1['text']=inp_file1.split('/')[len(inp_file1.split('/'))-1]	
	elif typer==2:
		inp_file2 = fl
		flabel2['text']=inp_file2.split('/')[len(inp_file2.split('/'))-1]
	elif typer==3:
		inp_file3 = fl
		flabel3['text']=inp_file3.split('/')[len(inp_file3.split('/'))-1]        

def readFile(typer,filen):
	print "readingg file*"
	global type_channel
	global sample_rate
	global sample_width
	global num_frames
	if typer==1:
		music_file = wave.open(filen, 'rb')
		type_channel1 = music_file.getnchannels()
		sample_rate1 = music_file.getframerate()
		sample_width1 = music_file.getsampwidth()
		num_frames1 = music_file.getnframes()

		raw_data = music_file.readframes( num_frames1 ) # Returns byte data
		music_file.close()
			## Formating raw_data into Integer data
		num_samples1 = num_frames1 * type_channel1

		if sample_width1 == 1:
			fmt = "%iB" % num_samples1 # read unsigned chars
		elif sample_width1 == 2:
			fmt = "%ih" % num_samples1 # read signed 2 byte shorts
		else:
			raise ValueError("Only supports 8 and 16 bit audio formats.")
		formated_data = list(struct.unpack(fmt, raw_data))
		return formated_data	
	elif typer == 2:
		music_file = wave.open(filen, 'rb')
		type_channel2 = music_file.getnchannels()
		sample_rate2 = music_file.getframerate()
		sample_width2 = music_file.getsampwidth()
		num_frames2 = music_file.getnframes()

		raw_data = music_file.readframes( num_frames2 ) # Returns byte data
		music_file.close()
			## Formating raw_data into Integer data
		num_samples2 = num_frames2 * type_channel2

		if sample_width == 1:
			fmt = "%iB" % num_samples2 # read unsigned chars
		elif sample_width == 2:
			fmt = "%ih" % num_samples2 # read signed 2 byte shorts
		else:
			raise ValueError("Only supports 8 and 16 bit audio formats.")
		formated_data = list(struct.unpack(fmt, raw_data))
		return formated_data	
	elif typer==3:
		music_file = wave.open(filen, 'rb')
		type_channel3 = music_file.getnchannels()
		sample_rate3 = music_file.getframerate()
		sample_width3 = music_file.getsampwidth()
		num_frames3 = music_file.getnframes()

		raw_data = music_file.readframes( num_frames3 ) # Returns byte data
		music_file.close()
			## Formating raw_data into Integer data
		num_samples3 = num_frames3 * type_channel3

		if sample_width3 == 1:
			fmt = "%iB" % num_samples3 # read unsigned chars
		elif sample_width == 2:
			fmt = "%ih" % num_samples3 # read signed 2 byte shorts
		else:
			raise ValueError("Only supports 8 and 16 bit audio formats.")
		formated_data = list(struct.unpack(fmt, raw_data))
		return formated_data	

	
def amplify(typer):
	print "amp file*"
	global r1
	global r2
	global r3
	max_amplification = 32767
	min_amplification = -32768
	#print self.scale11.get()
	if typer ==1:
		for i in xrange(len(r1)):
			if r1[i] * scale11.get() > max_amplification:
				r1[i] = max_amplification
			elif r1[i] * scale11.get() < min_amplification:
				r1[i] = min_amplification
			else:
				r1[i] = r1[i] * scale11.get()
	elif typer==2:
		for i in xrange(len(r2)):
			if r2[i] * scale21.get() > max_amplification:
				r2[i] = max_amplification
			elif r2[i] * scale21.get() < min_amplification:
				r2[i] = min_amplification
			else:
				r2[i] = r2[i] * scale21.get()
	elif typer==3:
		for i in xrange(len(r3)):
			if r3[i] * scale31.get() > max_amplification:
				r3[i] = max_amplification
			elif r3[i] * scale31.get() < min_amplification:
				r3[i] = min_amplification
			else:
				r3[i] = r3[i] * scale31.get()
def reversal(var,typer):
	print "reve file*"
	global r1
	global r2
	global r3
	if (var.get()) and (typer==1):
		#r1= r1[::-1]
		if type_channel1 == 1:
			r1.reverse()
		else:
			r1.reverse()
			for i in xrange(len(r1) - 1):
				temp = r1[i]
				r1[i] = r1[i+1]
				r1[i+1] = temp
	elif (var.get()) and (typer==2):
		#r2= r2[::-1]
		if type_channel2 == 1:
			r2.reverse()
		else:
			r2.reverse()
			for i in xrange(len(r2) - 1):
				temp = r2[i]
				r2[i] = r2[i+1]
				r2[i+1] = temp
		
	elif (var.get()) and (typer==3):
		#r3= r3[::-1]
		if type_channel3 == 1:
			r3.reverse()
		else:
			r3.reverse()
			for i in xrange(len(r3) - 1):
				temp = r3[i]
				r3[i] = r3[i+1]
				r3[i+1] = temp
	

'''def time_scaling():
	global r1
	r2=[]
	
	for i in xrange(len(r1)):'''
def time_shift(var,typer):
	print "shift file*"
	global r1
	global r2
	global r3
	global sample_width1
	global sample_rate1
	global num_frames1
	global type_channel1
	global sample_width2
	global sample_rate2
	global num_frames2
	global type_channel2
	global sample_width3
	global sample_rate3
	global num_frames3
	global type_channel3
	#print sample_rate
	operate = []
	if typer==1:
		operate = r1
		sample_width=sample_width1
		sample_rate=sample_rate1
		num_frames=num_frames1
		type_channel=type_channel1
	elif typer ==2:
		operate =r2
		sample_width=sample_width2
		sample_rate=sample_rate2
		num_frames=num_frames2
		type_channel=type_channel2
	elif typer == 3:
		operate =r3
		sample_width=sample_width3
		sample_rate=sample_rate3
		num_frames=num_frames3
		type_channel=type_channel3
	shift_frames=(var.get())*(sample_rate)
	shift_frames=int(shift_frames)
	if(var.get() > 0):
		print "negetive time shifting"
		if(type_channel == 1):
			a=[]
			#print shift_frames
			for i in range(shift_frames,0,-1):
				a.append(0)
			#print len(a)
			for i in range(0,len(r1)):
				a.append(r1[i])
			operate = a
		else:
			a=[]
			for i in range(2*shift_frames,0,-1):
				a.append(0)
			operate = a + operate
	else:
		if(type_channel == 1):
			operate=operate[shift_frames::1]
		else:
			operate=operate[2*shift_frames::1]
		print "positive time shifting"
	if typer==1:
		r1=operate
		num_frames1 = len(r1)/type_channel1	
	elif typer ==2:
		r2=operate
		num_frames2 = len(r2)/type_channel2
	else:
		r3=operate
		num_frames3 = len(r3)/type_channel3
	#num_frames = len(r1)/type_channel
def tscale(var,typer):
	print "scaling file*"
	global r1
	global r2
	global r3
	global sample_width1
	global sample_rate1
	global num_frames1
	global type_channel1
	global sample_width2
	global sample_rate2
	global num_frames2
	global type_channel2
	global sample_width3
	global sample_rate3
	global num_frames3
	global type_channel3
	operate=[]
	if typer==1:
		operate = r1
		sample_width=sample_width1
		sample_rate=sample_rate1
		num_frames=num_frames1
		type_channel=type_channel1
	elif typer ==2:
		operate =r2
		sample_width=sample_width2
		sample_rate=sample_rate2
		num_frames=num_frames2
		type_channel=type_channel2
	elif typer == 3:
		operate =r3
		sample_width=sample_width3
		sample_rate=sample_rate3
		num_frames=num_frames3
		type_channel=type_channel3
        a=[]
        sfactor=var.get()
        if(sfactor == 0):
            sfactor=1
	print sfactor
        if type_channel == 1:  
            k=int(len(operate)/sfactor)
            for i in range(k):
                a.append(operate[int(sfactor*i) ])
        else:
            e_li=[]
            o_li=[]
            for i in range( len(operate) ):
                if(i%2 == 0):
                    e_li.append(operate)
                else:
                    o_li.append(operate)
            k=int(len(e_li)/sfactor)
            for i in range(k):
                a.append(e_li[ int(sfactor*i) ])
                a.append(o_li[ int(sfactor*i) ])
	if typer==1:
		r1=a
		num_frames1 = len(r1)/type_channel1	
	elif typer ==2:
		r2=a
		num_frames2 = len(r2)/type_channel2
	else:
		r3=a
		num_frames3 = len(r3)/type_channel3

'''def mixing():
	SHRT_MIN=-32767 - 1
	SHRT_MAX=32767
	fl1=0
	fl2=0
	fl3=0
	
	if wave1.checkvar3.get()==1:		
		fl1=1
	if wave2.checkvar3.get()==1:
		fl2=1
	if wave3.checkvar3.get()==1:
		fl3=1
	if (fl1==1 & fl2==1) or (fl2==1 & fl3==1) or (fl1==1 & fl3==1):	
		if (fl1==1 & fl2==1):
			
		elif (fl1==1 & fl3==1):
			
		elif (fl2==1 & fl3==1):
			
		fo = wave.open("output.wav","w")
		fo.setparams(fi.getparams())
		width=fi.getsampwidth()
		width2=fi2.getsampwidth()	
		if width<width2:
			width=width2
		fmts=(None, "=B", "=h", None, "=l")
		fmt=fmts[width]
		dcs=(None, 128, 0, None, 0)
		dc=dcs[width]
		if fi.getnframes()>fi2.getnframes():
			maxi=fi.getnframes()
			flag=1		
		else:
			maxi=fi2.getnframes()
			flag=2
		amp=[]
		print flag
		for i in range(maxi):
			if flag==1 and i>=fi2.getnframes():
				if data[i]<SHRT_MIN: 
					iframe=SHRT_MIN
				elif data[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data[i]
			elif flag==2 and i>=fi.getnframes():
				if data2[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]
			else:
				if data2[i]+data[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]+data[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]+data[i]
			iframe-=dc
			oframe=iframe/2;
			oframe+=dc
			oframe=struct.pack(fmt, oframe)
			fo.writeframes(oframe)
		fi.close()
		fo.close()
		pl()
	elif (fl1==1 & fl2==1 & fl3==1):
		wave1.onread()
		cur=os.getcwd()
		cur+="output_file.wav"
		data=readfile(cur)
		fi = wave.open(cur,"rb")
		
		wave2.onread()
		cur=os.getcwd()
		cur+="output_file.wav"
		data2=readfile(cur)
		fi2 = wave.open(cur,"rb")
		
		wave3.onread()
		cur=os.getcwd()
		cur+="output_file.wav"
		data3=readfile(cur)	
		fi3 = wave.open(cur,"rb")
		fo = wave.open("output.wav","w")
		fo.setparams(fi.getparams())
		width=fi.getsampwidth()
		width2=fi2.getsampwidth()
		width3=fi3.getsampwidth()	
		if width<width2:
			width=width2
		if width<width3:
			width=width3
		fmts=(None, "=B", "=h", None, "=l")
		fmt=fmts[width]
		dcs=(None, 128, 0, None, 0)
		dc=dcs[width]
		if fi.getnframes()>fi2.getnframes():
			maxi=fi.getnframes()
			flag=1		
		else:
			maxi=fi2.getnframes()
			flag=2
		if fi3.getnframes()>maxi:
			maxi=fi3.getnframes()
			flag=3
		amp=[]
		for i in range(maxi):
			if flag==1 and i>=fi2.getnframes():
				if data[i]<SHRT_MIN: 
					iframe=SHRT_MIN
				elif data[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data[i]
			elif flag==2 and i>=fi.getnframes():
				if data2[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]
			elif flag==3 and i>=fi3.getnframes():
				if data3[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data3[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data3[i]
			else:
				if data2[i]+data[i]+data3[i]<SHRT_MIN:
					iframe=SHRT_MIN
				elif data2[i]+data[i]+data3[i]>SHRT_MAX:
					iframe=SHRT_MAX
				else:
					iframe=data2[i]+data[i]+data3[i]
			#	print int(iframe)
			iframe-=dc
			oframe=iframe/2;
			oframe+=dc
			oframe=struct.pack(fmt, oframe)
			fo.writeframes(oframe)
		fi.close()
		fo.close()
		pl()
		
def pl():
	chunk=1024
	cur=os.getcwd()
	cur+=str("/output.wav")
	wf = wave.open(cur, 'rb')
        p = pyaudio.PyAudio()
        stream = p.open(
            format = p.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True
        )
        data =wf.readframes(chunk)	
        while data != '':
            stream.write(data)
            data = wf.readframes(chunk)
	stream.close()
        p.terminate()
	'''
def save(typer):
	print "saving file*"
	global r1
	global r2
	global r3
	global sample_width1
	global sample_rate1
	global num_frames1
	global type_channel1
	global sample_width2
	global sample_rate2
	global num_frames2
	global type_channel2
	global sample_width3
	global sample_rate3
	global num_frames3
	global type_channel3
	if typer==1:
		if sample_width1==1:
		        fmt="%iB" % num_frames1*type_channel1
		else:
		        fmt="%ih" % num_frames1*type_channel1

		out_data=struct.pack(fmt,*(r1))
		print "making the thing"
		out_music_file=wave.open("ampli1.wav",'w')

		out_music_file.setframerate(sample_rate1)
		out_music_file.setnframes(num_frames1)
		out_music_file.setsampwidth(sample_width1)
		out_music_file.setnchannels(type_channel1)
		out_music_file.writeframes(out_data)

		out_music_file.close()
	elif typer==2:
		#print r2
		if sample_width2==1:
		        fmt="%iB" % num_frames2*type_channel2
		else:
		        fmt="%ih" % num_frames2*type_channel2

		out_data=struct.pack(fmt,*(r2))
		print "making the thing"
		out_music_file=wave.open("ampli2.wav",'w')

		out_music_file.setframerate(sample_rate2)
		out_music_file.setnframes(num_frames2)
		out_music_file.setsampwidth(sample_width2)
		out_music_file.setnchannels(type_channel2)
		out_music_file.writeframes(out_data)

		out_music_file.close()
	elif typer==3:
		#print r3
		if sample_width3==1:
		        fmt="%iB" % num_frames3*type_channel3
		else:
		        fmt="%ih" % num_frames3*type_channel3

		out_data=struct.pack(fmt,*(r3))
		print "making the thing"
		out_music_file=wave.open("ampli3.wav",'w')

		out_music_file.setframerate(sample_rate3)
		out_music_file.setnframes(num_frames3)
		out_music_file.setsampwidth(sample_width3)
		out_music_file.setnchannels(type_channel3)
		out_music_file.writeframes(out_data)

		out_music_file.close()
	#wf =wave.open('ampli.wav', 'rb')

def mixing(flaggy):
	global r1
	global r2
	global r3
	if flaggy:
		pflag=1		
		SHRT_MIN=-32767 - 1
		SHRT_MAX=32767
		fl1=0
		fl2=0
		fl3=0
		if rev12.get()==1:           
			fl1=1
		if rev22.get()==1:
			fl2=1
		if rev32.get()==1:
			fl3=1
		if (fl1==1 & fl2==1) or (fl2==1 & fl3==1) or (fl1==1 & fl3==1):
			if (fl1==1 & fl2==1):
				'''data=user1.readfile(1)
				data2=user2.readfile(2)
				fi = wave.open('output_file1.wav',"rb")
				fi2 = wave.open('output_file2.wav',"rb")'''
				r1 = readFile(1,inp_file1)
				r2 = readFile(2,inp_file2)
				amplify(1)
				reversal(rev1,1)
				time_shift(scale12,1)
				tscale(scale13,1)
				save(1)
				amplify(2)
				reversal(rev2,2)
				time_shift(scale22,1)
				tscale(scale23,2)
				save(2)
				fi = wave.open('ampli1.wav',"rb")
				fi2 = wave.open('ampli2.wav',"rb")
				data=r1
				data2=r2
			
		  	elif (fl1==1 & fl3==1):
				r1 = readFile(1,inp_file1)
				r3 = readFile(3,inp_file3)
				amplify(1)
				reversal(rev1,1)
				time_shift(scale12,1)
				tscale(scale13,1)
				save(1)
				amplify(3)
				reversal(rev3,3)
				time_shift(scale32,3)
				tscale(scale33,3)
				save(3)
				fi = wave.open('ampli1.wav',"rb")
				fi2 = wave.open('ampli3.wav',"rb")
				data=r1
				data2=r3
			elif (fl2==1 & fl3==1):
				r2 = readFile(2,inp_file2)
				r3 = readFile(3,inp_file3)
				amplify(3)
				reversal(rev3,3)
				time_shift(scale32,3)
				tscale(scale33,3)
				save(3)
				amplify(2)
				reversal(rev2,2)
				time_shift(scale22,1)
				tscale(scale23,2)
				save(2)
				fi = wave.open('ampli3.wav',"rb")
				fi2 = wave.open('ampli2.wav',"rb")
				data=r3
				data2=r2
			fo = wave.open("mixing.wav","w")
			fo.setparams(fi.getparams())
			width=fi.getsampwidth()
			width2=fi2.getsampwidth()      
			if width<width2:
				width=width2
			fmts=(None, "=B", "=h", None, "=l")
			fmt=fmts[width]
			dcs=(None, 128, 0, None, 0)
			dc=dcs[width]
			if fi.getnframes()>fi2.getnframes():
				maxi=fi.getnframes()
				flag=1         
			else:
				maxi=fi2.getnframes()
				flag=2
			amp=[]
			for i in range(maxi):
				if flag==1 and i>=fi2.getnframes():
					if data[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data[i]
				elif flag==2 and i>=fi.getnframes():
					if data2[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data2[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data2[i]
				else:
					if data2[i]+data[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data2[i]+data[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data2[i]+data[i]
				iframe-=dc
				oframe=iframe/2;
				oframe+=dc
				oframe=struct.pack(fmt, oframe)
				fo.writeframes(oframe)
		
			play2('mixing.wav')
		elif (fl1==1 & fl2==1 & fl3==1):
			'''data=user1.readfile(1)
			data2=user2.readfile(2)    
			data3=user3.readfile(3)
			fi = wave.open('output_file1.wav',"rb")
			fi2 = wave.open('output_file2.wav',"rb")
			fi3 = wave.open('output_file3.wav',"rb")'''
			r1 = readFile(1,inp_file1)
			r3 = readFile(3,inp_file3)
			r2 = readFile(2,inp_file2)
		
			amplify(1)
			reversal(rev1,1)
			time_shift(scale12,1)
			tscale(scale13,1)
			save(1)
		
			amplify(3)
			reversal(rev3,3)
			time_shift(scale32,3)
			tscale(scale33,3)
			save(3)
		
			amplify(2)
			reversal(rev2,2)
			time_shift(scale22,1)
			tscale(scale23,2)
			save(2)

			data=r1
			data2=r2
			data3=r3
				
			fi = wave.open('ampli1.wav',"rb")
			fi3 = wave.open('ampli3.wav',"rb")
			fi2 = wave.open('ampli2.wav',"rb")

			fo = wave.open("mixing.wav","w")
			fo.setparams(fi.getparams())
			width=fi.getsampwidth()
			width2=fi2.getsampwidth()
		 	width3=fi3.getsampwidth()      
		 	if width<width2:
		 		width=width2
		 	if width<width3:
				width=width3
			fmts=(None, "=B", "=h", None, "=l")
			fmt=fmts[width]
			dcs=(None, 128, 0, None, 0)
			dc=dcs[width]
			if fi.getnframes()>fi2.getnframes():
				maxi=fi.getnframes()
				flag=1         
			else:
				maxi=fi2.getnframes()
				flag=2
			if fi3.getnframes()>maxi:
				maxi=fi3.getnframes()
				flag=3
			amp=[]
			for i in range(maxi):
				if flag==1 and i>=fi2.getnframes():
					if data[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data[i]
				elif flag==2 and i>=fi.getnframes():
					if data2[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data2[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data2[i]
				elif flag==3 and i>=fi3.getnframes():
					if data3[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data3[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data3[i]
				else:
					if data2[i]+data[i]+data3[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data2[i]+data[i]+data3[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data2[i]+data[i]+data3[i]
	#       print int(iframe)
				iframe-=dc
				oframe=iframe/2;
				oframe+=dc
				oframe=struct.pack(fmt, oframe)
				fo.writeframes(oframe)
			play2('mixing.wav')
	else:
		pflag=0


def modulation(flaggy):
	global r1
	global r2
	global r3
	if flaggy:
		pflag=1		
		SHRT_MIN=-32767 - 1
		SHRT_MAX=32767
		fl1=0
		fl2=0
		fl3=0
		if rev13.get()==1:           
			fl1=1
		if rev22.get()==1:
			fl2=1
		if rev33.get()==1:
			fl3=1
		if (fl1==1 & fl2==1) or (fl2==1 & fl3==1) or (fl1==1 & fl3==1):
			if (fl1==1 & fl2==1):
				'''data=user1.readfile(1)
				data2=user2.readfile(2)
				fi = wave.open('output_file1.wav',"rb")
				fi2 = wave.open('output_file2.wav',"rb")'''
				r1 = readFile(1,inp_file1)
				r2 = readFile(2,inp_file2)
				amplify(1)
				reversal(rev1,1)
				time_shift(scale12,1)
				tscale(scale13,1)
				save(1)
				amplify(2)
				reversal(rev2,2)
				time_shift(scale22,1)
				tscale(scale23,2)
				save(2)
				fi = wave.open('ampli1.wav',"rb")
				fi2 = wave.open('ampli2.wav',"rb")
				data=r1
				data2=r2
			
		  	elif (fl1==1 & fl3==1):
				r1 = readFile(1,inp_file1)
				r3 = readFile(3,inp_file3)
				amplify(1)
				reversal(rev1,1)
				time_shift(scale12,1)
				tscale(scale13,1)
				save(1)
				amplify(3)
				reversal(rev3,3)
				time_shift(scale32,3)
				tscale(scale33,3)
				save(3)
				fi = wave.open('ampli1.wav',"rb")
				fi2 = wave.open('ampli3.wav',"rb")
				data=r1
				data2=r3
			elif (fl2==1 & fl3==1):
				r2 = readFile(2,inp_file2)
				r3 = readFile(3,inp_file3)
				amplify(3)
				reversal(rev3,3)
				time_shift(scale32,3)
				tscale(scale33,3)
				save(3)
				amplify(2)
				reversal(rev2,2)
				time_shift(scale22,1)
				tscale(scale23,2)
				save(2)
				fi = wave.open('ampli3.wav',"rb")
				fi2 = wave.open('ampli2.wav',"rb")
				data=r3
				data2=r2
			fo = wave.open("modulate.wav","w")
			fo.setparams(fi.getparams())
			width=fi.getsampwidth()
			width2=fi2.getsampwidth()      
			if width>width2:
				width=width2
			fmts=(None, "=B", "=h", None, "=l")
			fmt=fmts[width]
			dcs=(None, 128, 0, None, 0)
			dc=dcs[width]
			if fi.getnframes()<fi2.getnframes():
				maxi=fi.getnframes()
				flag=1         
			else:
				maxi=fi2.getnframes()
				flag=2
			amp=[]
			for i in range(maxi):
				if flag==1 and i>=fi2.getnframes():
					if data[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data[i]
				elif flag==2 and i>=fi.getnframes():
					if data2[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data2[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data2[i]
				else:
					if data2[i]*data[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data2[i]*data[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data2[i]*data[i]
				iframe-=dc
				oframe=iframe/2;
				oframe+=dc
				oframe=struct.pack(fmt, oframe)
				fo.writeframes(oframe)
		
			play1('modulate.wav')
		elif (fl1==1 & fl2==1 & fl3==1):
			'''data=user1.readfile(1)
			data2=user2.readfile(2)    
			data3=user3.readfile(3)
			fi = wave.open('output_file1.wav',"rb")
			fi2 = wave.open('output_file2.wav',"rb")
			fi3 = wave.open('output_file3.wav',"rb")'''
			r1 = readFile(1,inp_file1)
			r3 = readFile(3,inp_file3)
			r2 = readFile(2,inp_file2)
		
			amplify(1)
			reversal(rev1,1)
			time_shift(scale12,1)
			tscale(scale13,1)
			save(1)
		
			amplify(3)
			reversal(rev3,3)
			time_shift(scale32,3)
			tscale(scale33,3)
			save(3)
		
			amplify(2)
			reversal(rev2,2)
			time_shift(scale22,1)
			tscale(scale23,2)
			save(2)

			data=r1
			data2=r2
			data3=r3
				
			fi = wave.open('ampli1.wav',"rb")
			fi3 = wave.open('ampli3.wav',"rb")
			fi2 = wave.open('ampli2.wav',"rb")

			fo = wave.open("modulate.wav","w")
			fo.setparams(fi.getparams())
			width=fi.getsampwidth()
			width2=fi2.getsampwidth()
		 	width3=fi3.getsampwidth()      
		 	if width>width2:
		 		width=width2
		 	if width>width3:
				width=width3
			fmts=(None, "=B", "=h", None, "=l")
			fmt=fmts[width]
			dcs=(None, 128, 0, None, 0)
			dc=dcs[width]
			if fi.getnframes()<fi2.getnframes():
				maxi=fi.getnframes()
				flag=1         
			else:
				maxi=fi2.getnframes()
				flag=2
			if fi3.getnframes()<maxi:
				maxi=fi3.getnframes()
				flag=3
			amp=[]
			for i in range(maxi):
				if flag==1 and i>=fi2.getnframes():
					if data[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data[i]
				elif flag==2 and i>=fi.getnframes():
					if data2[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data2[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data2[i]
				elif flag==3 and i>=fi3.getnframes():
					if data3[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data3[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data3[i]
				else:
					if data2[i]*data[i]*data3[i]<SHRT_MIN:
						iframe=SHRT_MIN
					elif data2[i]*data[i]*data3[i]>SHRT_MAX:
						iframe=SHRT_MAX
					else:
						iframe=data2[i]*data[i]*data3[i]
	#       print int(iframe)
				iframe-=dc
				oframe=iframe/2;
				oframe+=dc
				oframe=struct.pack(fmt, oframe)
				fo.writeframes(oframe)
			play1('modulate.wav')
	else:
		pflag=0
def record():
	chunk=1024
	arr=[]
	FORMAT=pyaudio.paInt16
	channelsit=1
	rateit=44100
	record_seconds=5
	p=pyaudio.PyAudio()
	stream=p.open(format=FORMAT, channels=channelsit,rate=rateit,input=True,output=True,frames_per_buffer=chunk)
	for i in range(0,44100/chunk*record_seconds):
		data=stream.read(chunk)
		arr.append(data)
	wf=wave.open("rec.wav",'wb')
	wf.setnchannels(channelsit)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(rateit)
	wf.writeframes(b''.join(arr))
	wf.close()
	stream.stop_stream()
	stream.close()
	p.terminate()
def pl1():
	chunk=1024
	cur=os.getcwd()
	cur+=str("/rec.wav")
	wf=wave.open(cur,'rb')
	p=pyaudio.PyAudio()
	stream=p.open(
		format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True
	)
	data=wf.readframes(chunk)
	while data!= '':
		stream.write(data)
		data=wf.readframes(chunk)
	stream.close()
	p.terminate()

root = Tk()
screen_x=root.winfo_screenwidth()
screen_y=root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (900, 600, (screen_x-900)/2, (screen_y-600)/2))
w=Label(root,text="Wave Mixer",width=10,height=3,font=35)
w.pack()

#frame 1
#frame_m=Frame(root)
#frame_m.pack(side=LEFT,fill=None,expand=True)
labelframe1 = LabelFrame(root, text="Wave 1")
labelframe1.pack(side=LEFT,fill="both", expand="yes")
######################################################
button = Button(labelframe1, text="Select File", fg="red",command=lambda :open_file(1))
button.pack(side=TOP)
flabel1=Label(labelframe1,text='')
flabel1.pack(side=TOP)
#if w_name=='':
#	b = Button(labelframe1, text="Play", state="disabled",command=lambda :play(1))
#	b.pack()
#else:
#	b = Button(labelframe1, text="Play", command=lambda :play(1))
#	b.pack()


#
amp1=DoubleVar()
scale11=Scale(labelframe1,label="Amplitude",from_=0,to=5,resolution=0.5,variable=amp1,orient=HORIZONTAL)
scale11.pack(side=TOP)

#timeshift Scale 
sh1=DoubleVar()
scale12=Scale(labelframe1,label="Time Shift",from_=-5,to=5,resolution=0.5,variable=sh1,orient=HORIZONTAL)
scale12.pack(side=TOP)
#timescale Scale 
ts1=DoubleVar()
scale13=Scale(labelframe1,label="Time Scaling",from_=0,to=8,resolution=0.125,variable=ts1,orient=HORIZONTAL)
scale13.pack(side=TOP)
#Time Reversal 
rev1=IntVar()
c1=Checkbutton(labelframe1,text="Time Reversal",variable=rev1,onvalue=1,offvalue=0,height=3,width=20)
c1.pack(side=TOP)
rev12=IntVar()
c12=Checkbutton(labelframe1,text="Mixing",variable=rev12,onvalue=1,offvalue=0,height=3,width=20)
c12.pack(side=TOP)
rev13=IntVar()
c13=Checkbutton(labelframe1,text="Modulate",variable=rev13,onvalue=1,offvalue=0,height=3,width=20)
c13.pack(side=TOP)
#
b = Button(labelframe1, text="Play", command=lambda :prep(1,inp_file1))
b.pack()
b = Button(labelframe1, text="Stop", command=lambda: prep(0,inp_file1))
b.pack()
'''
progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200,maximum = 0.1, variable=one_prog)
progressbar.pack(side=TOP)
progressbar.start()
'''
#cb = Checkbutton(root, text="Show title")
#cb.select()
#cb.place(x=50, y=150)

#frame 2
#frame_2=Frame(root)
#frame_2.pack(side=LEFT,fill=None,expand=True)
labelframe2 = LabelFrame(root, text="Wave 2")
labelframe2.pack(side=LEFT,fill="both", expand="yes")
button = Button(labelframe2, text="Select File", fg="red",command=lambda :open_file(2))
button.pack(side=TOP)
flabel2=Label(labelframe2,text='')
flabel2.pack(side=TOP)
#
amp2=DoubleVar()
scale21=Scale(labelframe2,label="Amplitude",from_=0,to=5,resolution=0.5,variable=amp2,orient=HORIZONTAL)
scale21.pack(side=TOP)

sh2=DoubleVar()
scale22=Scale(labelframe2,label="Time Shift",from_=-5,to=5,resolution=0.5,variable=sh2,orient=HORIZONTAL)
scale22.pack(side=TOP)

ts2=DoubleVar()
scale23=Scale(labelframe2,label="Time Scaling",from_=0,to=8,resolution=0.125,variable=ts2,orient=HORIZONTAL)
scale23.pack(side=TOP)

rev2=IntVar()
c2=Checkbutton(labelframe2,text="Time Reversal",variable=rev2,onvalue=1,offvalue=0,height=3,width=20)
c2.pack(side=TOP)
rev22=IntVar()
c22=Checkbutton(labelframe2,text="Mixing",variable=rev22,onvalue=1,offvalue=0,height=3,width=20)
c22.pack(side=TOP)
rev23=IntVar()
c23=Checkbutton(labelframe2,text="Modulate",variable=rev23,onvalue=1,offvalue=0,height=3,width=20)
c23.pack(side=TOP)

b = Button(labelframe2, text="Play", command=lambda :prep(2,inp_file2))
b.pack()
b = Button(labelframe2, text="Stop", command=lambda: prep(0,inp_file2))
b.pack()
#
#frame 3
#frame_3=Frame(root)
#frame_3.pack(side=LEFT,fill=None,expand=True)
labelframe3 = LabelFrame(root, text="Wave 3")
labelframe3.pack(side=LEFT,fill="both", expand="yes")
button = Button(labelframe3, text="Select File", fg="red",command=lambda :open_file(3))
button.pack(side=TOP)
flabel3=Label(labelframe3,text='')
flabel3.pack(side=TOP)
#

amp3=DoubleVar()
scale31=Scale(labelframe3,label="Amplitude",from_=0,to=5,resolution=0.5,variable=amp3,orient=HORIZONTAL)
scale31.pack(side=TOP)

sh3=DoubleVar()
scale32=Scale(labelframe3,label="Time Shift",from_=-5,to=5,resolution=0.5,variable=sh3,orient=HORIZONTAL)
scale32.pack(side=TOP)

ts3=DoubleVar()
scale33=Scale(labelframe3,label="Time Scaling",from_=0,to=8,resolution=0.125,variable=ts3,orient=HORIZONTAL)
scale33.pack(side=TOP)

rev3=IntVar()
c3=Checkbutton(labelframe3,text="Time Reversal",variable=rev3,onvalue=1,offvalue=0,height=3,width=20)
c3.pack(side=TOP)

rev32=IntVar()
c32=Checkbutton(labelframe3,text="Mixing",variable=rev32,onvalue=1,offvalue=0,height=3,width=20)
c32.pack(side=TOP)
rev33=IntVar()
c33=Checkbutton(labelframe3,text="Modulate",variable=rev33,onvalue=1,offvalue=0,height=3,width=20)
c33.pack(side=TOP)

b = Button(labelframe3, text="Play", command=lambda :prep(3,inp_file3))
b.pack()
b = Button(labelframe3, text="Stop", command=lambda: prep(0,inp_file3))
b.pack()
#######################################################
# Code to add widgets will go here...
labelframe4 = LabelFrame(root, text="Other Operations")
labelframe4.pack(side=LEFT,fill="both", expand="yes")
b = Button(labelframe4, text="Mixing and Play", command=lambda :mixing(1))
b.pack(side = TOP)

b = Button(labelframe4, text="Modulate and Play", command=lambda: modulation(1))
b.pack(side = BOTTOM)
buttonit2=Button(labelframe4,text="Record",command=record,fg="brown")
buttonit2.pack(side=LEFT)
buttonit3=Button(labelframe4,text="Play",command=pl1,fg="brown")
buttonit3.pack(side=LEFT)

root.mainloop()
