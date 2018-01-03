# py_gamepad
Reading Wireless gamepad input and translate it on GIPO

linux console:

pip install bitarray / pip3 install bitarray
sudo apt-get install python-dev




1. bitarray
The bitarray class:

bitarray([initial], [endian=string])
Return a new bitarray object whose items are bits initialized from the optional initial, and endianness. If no object is provided, the bitarray is initialized to have length zero. The initial object may be of the following types:

int, long
Create bitarray of length given by the integer. The initial values in the array are random, because only the memory allocated.
string
Create bitarray from a string of ‘0’s and ‘1’s.
list, tuple, iterable
Create bitarray from a sequence, each element in the sequence is converted to a bit using truth value value.
bitarray
Create bitarray from another bitarray. This is done by copying the memory holding the bitarray data, and is hence very fast.
The optional keyword arguments ‘endian’ specifies the bit endianness of the created bitarray object. Allowed values are ‘big’ and ‘little’ (default is ‘big’).

Note that setting the bit endianness only has an effect when accessing the machine representation of the bitarray, i.e. when using the methods: tofile, fromfile, tobytes, frombytes.

A bitarray object supports the following methods:

all() -> bool
Returns True when all bits in the array are True.
any() -> bool
Returns True when any bit in the array is True.
append(item)
Append the value bool(item) to the end of the bitarray.
buffer_info() -> tuple
Return a tuple (address, size, endianness, unused, allocated) giving the current memory address, the size (in bytes) used to hold the bitarray’s contents, the bit endianness as a string, the number of unused bits (e.g. a bitarray of length 11 will have a buffer size of 2 bytes and 5 unused bits), and the size (in bytes) of the allocated memory.
bytereverse()
For all bytes representing the bitarray, reverse the bit order (in-place). Note: This method changes the actual machine values representing the bitarray; it does not change the endianness of the bitarray object.
copy() -> bitarray
Return a copy of the bitarray.
count([value]) -> int
Return number of occurrences of value (defaults to True) in the bitarray.
decode(code) -> list
Given a prefix code (a dict mapping symbols to bitarrays), decode the content of the bitarray and return the list of symbols.
encode(code, iterable)
Given a prefix code (a dict mapping symbols to bitarrays), iterates over iterable object with symbols, and extends the bitarray with the corresponding bitarray for each symbols.
endian() -> string
Return the bit endianness as a string (either ‘little’ or ‘big’).
extend(object)
Append bits to the end of the bitarray. The objects which can be passed to this method are the same iterable objects which can given to a bitarray object upon initialization.
fill() -> int
Adds zeros to the end of the bitarray, such that the length of the bitarray is not a multiple of 8. Returns the number of bits added (0..7).
frombytes(bytes)
Append from a byte string, interpreted as machine values.
fromfile(f, [n])
Read n bytes from the file object f and append them to the bitarray interpreted as machine values. When n is omitted, as many bytes are read until EOF is reached.
fromstring(string)
Append from a string, interpreting the string as machine values. Deprecated since version 0.4.0, use frombytes() instead.
index(value, [start, [stop]]) -> int
Return index of the first occurrence of bool(value) in the bitarray. Raises ValueError if the value is not present.
insert(i, item)
Insert bool(item) into the bitarray before position i.
invert()
Invert all bits in the array (in-place), i.e. convert each 1-bit into a 0-bit and vice versa.
iterdecode(code) -> iterator
Given a prefix code (a dict mapping symbols to bitarrays), decode the content of the bitarray and iterate over the symbols.
itersearch(bitarray) -> iterator
Searches for the given a bitarray in self, and return an iterator over the start positions where bitarray matches self.
length() -> int
Return the length, i.e. number of bits stored in the bitarray. This method is preferred over __len__ (used when typing len(a)), since __len__ will fail for a bitarray object with 2^31 or more elements on a 32bit machine, whereas this method will return the correct value, on 32bit and 64bit machines.
pack(bytes)
Extend the bitarray from a byte string, where each characters corresponds to a single bit. The character b’x00’ maps to bit 0 and all other characters map to bit 1. This method, as well as the unpack method, are meant for efficient transfer of data between bitarray objects to other python objects (for example NumPy’s ndarray object) which have a different view of memory.
pop([i]) -> item
Return the i-th (default last) element and delete it from the bitarray. Raises IndexError if bitarray is empty or index is out of range.
remove(item)
Remove the first occurrence of bool(item) in the bitarray. Raises ValueError if item is not present.
reverse()
Reverse the order of bits in the array (in-place).
search(bitarray, [limit]) -> list
Searches for the given a bitarray in self, and returns the start positions where bitarray matches self as a list. The optional argument limits the number of search results to the integer specified. By default, all search results are returned.
setall(value)
Set all bits in the bitarray to bool(value).
sort(reverse=False)
Sort the bits in the array (in-place).
to01() -> string
Return a string containing ‘0’s and ‘1’s, representing the bits in the bitarray object. Note: To extend a bitarray from a string containing ‘0’s and ‘1’s, use the extend method.
tobytes() -> bytes
Return the byte representation of the bitarray. When the length of the bitarray is not a multiple of 8, the few remaining bits (1..7) are set to 0.
tofile(f)
Write all bits (as machine values) to the file object f. When the length of the bitarray is not a multiple of 8, the remaining bits (1..7) are set to 0.
tolist() -> list
Return an ordinary list with the items in the bitarray. Note that the list object being created will require 32 or 64 times more memory than the bitarray object, which may cause a memory error if the bitarray is very large. Also note that to extend a bitarray with elements from a list, use the extend method.
tostring() -> string
Return the string representing (machine values) of the bitarray. When the length of the bitarray is not a multiple of 8, the few remaining bits (1..7) are set to 0. Deprecated since version 0.4.0, use tobytes() instead.
unpack(zero=b'\x00', one=b'\xff') -> bytes
Return a byte string containing one character for each bit in the bitarray, using the specified mapping. See also the pack method.
Functions defined in the module:

test(verbosity=1, repeat=1) -> TextTestResult
Run self-test, and return unittest.runner.TextTestResult object.
bitdiff(a, b) -> int
Return the difference between two bitarrays a and b. This is function does the same as (a ^ b).count(), but is more memory efficient, as no intermediate bitarray object gets created
bits2bytes(n) -> int
Return the number of bytes necessary to store n bits.
