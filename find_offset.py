from pwn import *
import sys

context.log_level = 'ERROR'
		
def try_input2(left, right):
	found = 0
	interval = []
		
	while found == 0:
		p = process("./" + sys.argv[1])
		
		try:
			p.sendline(b"A" * right)
			resp = p.recv()
			
			left = right
			right += 1000
		except:
			p.close()
			found = 1
			interval = [left, right]
	
	print(f"Found interval: {interval}")
	
	found = 0
	
	while True:
		if right - left <= 10:
			break
			
		p = process("./" + sys.argv[1])
			
		try:
			center = int((right + left) / 2)
			p.sendline(b"A" * center)
			resp = p.recv()
			
			left = center
		except:
			p.close()
			right = center
			
	for i in range(left, right + 1):
		p = process("./" + sys.argv[1])
		
		try:
			p.sendline(b"A" * i)
			resp = p.recv()
		except:
			p.close()
			print(f"Found offset at {i + 1}")
			break

if __name__ == "__main__":
	if len(sys.argv) == 2:
		try_input2(1, 1000)
			
	else:
		print("Usage: python3 find_offset.py name_of_your_application")
	
