import random

SUMPOWERSOF7 = 'SUMPOWERSOF7'
FIRSTNBYTES = 'FIRSTNBYTES'
SHUFFLE = 'SHUFFLE'
BORINGTEST = 'BORING'
COMPLETELYRANDOM = "COMPLETELYRANDOM"
LONGPATTERNS = "LONGPATTERNS"
LESSVARIABLERANDOM = "LESSVARIABLERANDOM"

# dedup / redup methodology
##
# ###  dedup
# accepts a file path as input and does the following to the file to write to a file path passed as output:
# assigns a hash value to each block and creates an in memory table of hash values which should be substantially less than the file length
# write the hash table to the output file
# for each block in the input file, write out its hash to the output file
##
# ###  redup
# accepts a file path as input and does the following to the file to write to a file path passed as output:
# reads in a hash table from the input file
# for each block in the input file after the hash table, convert the block to a longer block using the hash table
# and write it to the output file

class dedupredup:
    # __init__ creates dedupredup object
    def __init__(self, cz, hz,debugflag, hashfunc, testyp,origfilepath, dedupfilepath, redupfilepath):
        self.SUMPOWERSOF7 = 'SUMPOWERSOF7'      # hash method just sum of powers of 7
        self.FIRSTNBYTES = 'FIRSTNBYTES'        # hash method first n bytes of block
        self.SHUFFLE = 'SHUFFLE'                # hash method just sum of various methods determined by 3 bits
        self.hashfunc = hashfunc                # this is the hash function which will be used in dedup [assigned by parameter]
        self.hashtable ={}                      # this table stores hashes and value
        self.orderedhashes = []                 # stores ordered hashes for purposes of writing file
        self.chunksize  =cz                     # parameter assigned size of chunk [1024 bytes for this use case]
        self.hashsize = hz                      # parameter assigned size of hash code [8 bytes per chunk for this use case]
        self.attempts =0                        # statistics on how many hash attempts were made
        self.matches = 0                        # statisics on how many hashes and values matched [or hit] and existing value
        self.collisions = 0                     # collisions on how many hashes overlapped for different values
        self.debughash = debugflag              # DEPRECATED : debug flag, TODO add debugs in in a meaningful way
        self.testtype = testyp                  # this is the name of the type of file which will be generated to test the process
        self.originalfilepath = origfilepath    # original or source binary file location and name
        self.dedupedfilepath = dedupfilepath    # deduped binary file location and name
        self.redupedfilepath = redupfilepath    # reduped binary file location and name

# START my hash function dictionary
    # accepts a block to hash
    # returns a number with bytes within hashsize
    # simply sum up powers of 7
    def sumpowersof7ofordtimeslen(self, blocktohash):
        total = 0
        hashreturn = ""
        for i in range(len(blocktohash)):
            total += ord(blocktohash[i]) * (7 ** i)
        #print("total", total)
        #print('modula', (self.hashsize * 8) ** 2)
        #print((len(blocktohash) * total) %  ((self.hashsize * 8) ** 2))
        #print(( total) % ((self.hashsize * 8) ** 2))
        z = (len(blocktohash) * total) %  ((self.hashsize * 8) ** 2)
        z= (( total) % ((self.hashsize * 8) ** 2))
        return z

    # accepts a block to hash
    # returns a number with bytes within hashsize
    def firstnbyteshashfun(self, blocktohash):
        # accepts a block to hash
        # returns a number with bytes within hashsize
        hashreturn = 0
        x = blocktohash[0:self.hashsize]
        for i in range(len(x)):
            hashreturn = hashreturn + ord(x[i])
        return hashreturn % (self.hashsize * 8) ** 2

    # accepts a block to hash
    # returns a number with bytes within hashsize
    # use a different strategy per 3 bits to make a large number to create hash
    def shuffleandsplit(self, blocktohash):
        hashreturn =0
        usefun = '{0:08b}'.format(int(blocktohash[1]))
        usefun = list(usefun)
        usefun.reverse()
        usefun = usefun[0:3]
        option = ''.join(usefun)
        optionnum = int(option,2)
        hashreturn=0
        if optionnum == 0:
            for i in range(len(blocktohash)):
                hashreturn = hashreturn + blocktohash[i]**4
        if optionnum == 1:
            for i in range(len(blocktohash)):
                hashreturn = hashreturn + blocktohash[i]*blocktohash[2]**blocktohash[3]
        if optionnum == 2:
            for i in range(len(blocktohash)):
                hashreturn = hashreturn + blocktohash[i]//3**12
        if optionnum == 3:
            for i in range(len(blocktohash)):
                hashreturn = hashreturn + blocktohash[i]**10
        if optionnum == 4:
            for i in range(len(blocktohash)):
                hashreturn + hashreturn + blocktohash[i]**2
        if optionnum == 5:
            for i in range(len(blocktohash)):
                hashreturn = hashreturn + blocktohash[i]**2
        if optionnum == 6:
            for i in range(len(blocktohash)):
                hashreturn = hashreturn + blocktohash[i]**3
        if optionnum == 7:
            for i in range(len(blocktohash)):
                hashreturn = hashreturn + blocktohash[i]**4
        return hashreturn % 2**(self.hashsize * 8)
# END my hash function dictionary

    #make hash
    #calls a hash function with a block or chunk, gets a number, turns the number into binary and into a string
    def make_hash(self,blocktohash,debughashfunct=""):
        # accepts input of size blocksize
        # returns a hash of size hashsize
        # debughashfunct is deprecated
        if self.hashfunc == SUMPOWERSOF7:
            z = self.sumpowersof7ofordtimeslen(blocktohash)
        if self.hashfunc == FIRSTNBYTES:
            z = self.firstnbyteshashfun(blocktohash)
        if self.hashfunc == SHUFFLE:
            z = self.shuffleandsplit(blocktohash)
        hashreturn = ""
        zbinary = "{0:b}".format(z)
        zzbinary = zbinary.rjust(self.hashsize*8,'0')[-self.hashsize*8:]
        for hashcount in range(0,self.hashsize):
            xchar = zzbinary[hashcount * 8:hashcount * 8 + 7]
            xval = int(xchar,2)
            hashreturn = hashreturn + chr(xval)
        return hashreturn

    #add hash to hash table
    #puts hash key in hashtable with original value the hash can go back to, records status
    def add_hash_to_hashtable(self,hash,value):
        self.attempts += 1
        if hash not in self.hashtable.keys():
            self.hashtable[hash] = value
            status = "New"
        else:
            if hash in self.hashtable.keys() and self.hashtable[hash] == value:
                self.matches +=1
                status = "Matched"
            else:
                self.collisions+=1
                status = "Collision"
        return status

    #output contents of hashtable
    def print_hashtable(self):
        print('hashtable')
        print(self.hashtable)

    # return the string value for a hash
    def get_hashtable_lookup(self, hash):
        return self.hashtable[hash]

    # construct hash table from raw data using dedupredup object settings for a given raw data and index from file
    def add_hash_to_lookup(self,writefile, rawdata, ind):
        hashed_value = self.make_hash(rawdata,self.debughash)
        hashstatus = self.add_hash_to_hashtable(hashed_value,rawdata)
        if hashstatus == "New":
            writefile.write("hash then raw\r\n".encode())
            writefile.write(hashed_value.encode()+"\r\n".encode())
            writefile.write(rawdata+"\r\n".encode())
        self.orderedhashes.append(hashed_value)

    # return a chunk from a string given an index
    def readind(self,x,longstring):
        return longstring[x:x+self.chunksize]

    # remove duplicates from a file by constructing a hash table and file table to represent the file
    def dedup(self,inputpath,outputpath):
        print("DEDUP: opening files for reading and writing")
        input_file = open(inputpath, "rb")
        outfile = open(outputpath, "wb")
        indcount = 0
        block = input_file.read(1024)
        while block != b"":
            for chunkstart in range(0, len(block), self.chunksize):
                chunk = self.readind(chunkstart, block)
                self.add_hash_to_lookup(outfile, chunk, indcount)
            indcount += 1
            block = input_file.read(1024)
        for i in self.orderedhashes:
            outfile.write(i.encode())
        outfile.write("\r\n".encode())
        outfile.close()
        input_file.close()
        return 'deduped ' + str(indcount) + ' chunks'

    # output stats for hashing a file
    def stats(self):
        print('collisions', self.collisions)
        print('attempts' , self.attempts)
        print('matches', self.matches)
        print('total bits used', self.hashsize*8)
        print('potential combinations', (self.hashsize*8)**2)
        self.print_hashtable()
        print('error',self.collisions/self.attempts)

# START METHODS to create test files
    def createrandomtestfile(self,outpath,  num_of_blocks):
        longstring =""
        output_file = open(outpath, "wb")
        ## create a block of random numbers and write to file
        for i in range(1024*num_of_blocks):
            longstring = longstring + str(random.randint(0, 9))
        output_file.write(longstring.encode())
        #closing file
        output_file.close()
        return num_of_blocks

    def createboringtestfile(self,outpath,  num_of_blocks):
        longstring =""
        print("writing boring test file")
        output_file = open(outpath, "wb")
        ## create a block of zeros and write to file
        for i in range(1024*num_of_blocks):
            longstring = longstring + '0'
        output_file.write(longstring.encode())
        #closing file
        output_file.close()
        return num_of_blocks

    def createverylongpatterns(self,outpath,numofpatternblocks):
        longstring =""
        print("writing boring test file")
        output_file = open(outpath, "wb")
        ## create blocks of zeros and write to file
        for i in range(1024*8):
            longstring = longstring + '0'
        ## create blocks of ones and write to file
        for i in range(1024*8):
            longstring = longstring + '1'
        ## create blocks of zeros and write to file
        for i in range(1024*8):
            longstring = longstring + '0'
        ## create blocks of ones and write to file
        for i in range(1024*8):
            longstring = longstring + '1'
        ## create blocks of zeros and write to file
        output_file.write(longstring.encode())
        #closing file
        output_file.close()
        return numofpatternblocks

    def createmuchlessvariablerandomtestfile(self,outpath,  num_of_blocks):
        longstring =""
        outint = 0
        outchar = ""
        output_file = open(outpath, "wb")

        ## create a block of random numbers and write to file
        for j in range(num_of_blocks):
            outint = abs(1-outint)
            outchar = str(outint)
            for i in range(1024*num_of_blocks):
                longstring = longstring + outchar
        output_file.write(longstring.encode())
        #closing file
        output_file.close()
        return num_of_blocks

# END METHODS to create test files
    # redup the inputf file into the outputf file
    def redup(self,inputf, outputf):
        print('redupping')
        self.hashtable = {}
        #read hash table
        finput = open(inputf,"rb")
        foutput = open(outputf,"wb")
        #read hash table
        print("reading deduped file")
        # load hash table
        inputline = finput.readline()[:-2]
        while inputline == b'hash then raw':
            filehashkey = finput.readline()[:-2]
            filehashvalue = finput.readline()[:-2]
            self.hashtable[filehashkey] = filehashvalue
            inputline = finput.readline()[:-2]
        self.stats()
        # go through file contents and map file out of hash table
        for i in range(0,len(inputline)//self.hashsize):
            decodethis = inputline[i*self.hashsize:i*self.hashsize+self.hashsize]
            foutput.write(self.hashtable[decodethis])
        foutput.close()
        finput.close()
        # output if any error is expected due to collisions
        if self.collisions > 0:
            return "complete with collisions %d \n" % self.collisions
        return "complete"

# used to print out a file
def outputfile(inpath):
    finput = open(inpath, "rb")
    x = finput.readline()
    print(x)
    finput.close()

#execute tests
if __name__ == '__main__':
    # create a dedupredup object for testing
    # block size = 1024, hash size of 8 bytes per 1024 bytes
    # deprecated debug flag is set to True
    # algorithm for hashing is Shuffle
    # algorithm for creating test file is LESSVARIABLERANDOM
    # original file path and file name is "myoriginalfile.bin"
    # deduped file path and file name is "mydedupedfile.bin"
    # reduped file path and file name is "myredupedfile.bin"
    dduprdup = dedupredup(1024,8,True,SHUFFLE, LESSVARIABLERANDOM, "myoriginalfile.bin", "mydedupedfile.bin", "myredupedfile.bin")

    # choose based on the test file type algorithm, create a test file in the original file path
    if dduprdup.testtype == BORINGTEST:
        z = dduprdup.createboringtestfile(dduprdup.originalfilepath, 4)
    if dduprdup.testtype == COMPLETELYRANDOM:
        z= dduprdup.createrandomtestfile(dduprdup.originalfilepath,4)
    if dduprdup.testtype == LONGPATTERNS:
        z= dduprdup.createverylongpatterns(dduprdup.originalfilepath,8)
    if dduprdup.testtype == LESSVARIABLERANDOM:
        z = dduprdup.createmuchlessvariablerandomtestfile(dduprdup.originalfilepath, 20)

    # dedup the file in the original file path into the deduped file path
    print(dduprdup.dedup(dduprdup.originalfilepath, dduprdup.dedupedfilepath))
    # redup the file in the deduped file path into the reduped file path
    print(dduprdup.redup(dduprdup.dedupedfilepath,  dduprdup.redupedfilepath)) # was output_string = a.redup()
