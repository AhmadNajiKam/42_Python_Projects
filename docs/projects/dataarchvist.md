# DataArchivist

**Folder:** `DataArchivist/`  
**Theme:** File stream management — context managers, binary vs text mode, stream buffering  
**Key file:** `archivist.py`

---

## Core Patterns

### Reading files safely

```python
with open("archive.txt", "r", encoding="utf-8") as f:
    content = f.read()
# File is automatically closed even if an exception is raised
```

Always specify `encoding="utf-8"` explicitly — the default encoding is platform-dependent (Windows uses `cp1252` by default).

### Binary mode

For non-text files (images, compressed archives, pickled data):

```python
with open("data.bin", "rb") as f:
    header = f.read(4)   # read exactly 4 bytes
    rest = f.read()

with open("output.bin", "wb") as f:
    f.write(b"\x89PNG\r\n")
```

### Line-by-line iteration (memory-efficient)

For large files, don't load everything into memory:

```python
with open("large.log", "r", encoding="utf-8") as f:
    for line in f:                # file object is an iterator
        process(line.rstrip("\n"))
```

### Writing and appending

```python
# Overwrite
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("fresh content\n")

# Append
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("new entry\n")
```

---

## Stream Positions

```python
with open("data.txt", "r+", encoding="utf-8") as f:
    f.seek(0)           # move to start
    content = f.read()
    f.seek(0, 2)        # move to end (whence=2)
    pos = f.tell()      # current byte position
```

---

## Lessons Learned

- **Always use context managers** (`with open(...)`) — `f.close()` in a `finally` block is verbose and easy to forget.
- **Binary vs text mode matters** — opening a `.png` in text mode on Windows silently corrupts `\r\n` sequences.
- **`encoding="utf-8"` is not optional** — hardcode it; never rely on the system default.
- **Large files = iterator** — `f.readlines()` loads the whole file into RAM; `for line in f` streams it lazily.
