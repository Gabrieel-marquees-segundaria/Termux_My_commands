from modules.zip_manager import ZipManager
import sys

zip = ZipManager()

def setup():
    pass

if __name__ == "__main__":
   args = sys.argv
   # for arg in sys.argv:
   #    print(arg)
   print(len(sys.argv))
   print(args)
   if "extract" in sys.argv[1]:
      if sys.argv[2] and sys.argv[3]:
         from_path = sys.argv[4] if len(sys.argv) == 5 else "~/bin/temp"
         zip.extract_path(sys.argv[2], sys.argv[3], from_path)
   if "build" in sys.argv[1]:
      pass
   if "rm" in sys.argv[1]:
      zip.remove_temp_dir()
