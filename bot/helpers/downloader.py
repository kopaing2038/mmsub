import os
import wget
import glob
import sys
import youtube_dl
import urllib.request
from pySmartDL import SmartDL
from urllib.error import HTTPError
from youtube_dl import DownloadError
from bot import DOWNLOAD_DIRECTORY, LOGGER


def download_file(url, dl_path):
  try:
    dl = SmartDL(url, dl_path, progress_bar=False)
    LOGGER.info(f'Downloading: {url} in {dl_path}')
    dl.start()
    return True, dl.get_dest()
  except HTTPError as error:
    return False, error
  except Exception as error:
    try:
      filename = wget.download(url, dl_path)
      return True, os.path.join(f"{DOWNLOAD_DIRECTORY}/{filename}")
    except HTTPError:
      return False, error

def download_fmax(url, dl_path):
  try:
    filename = wget.download(url, dl_path)

    return True
  except HTTPError:
    return False
def download_poster(url, dl_path):

  opener = urllib.request.URLopener()
  opener.addheader('User-Agent', 'whateveyuyr')
  filename = dl_path + "/thumb.jpg"
  try:
      r = opener.retrieve(url, filename)
  except HTTPError:
      Error = "Cannot Download"
      return Error

def utube_dl(link):
  ytdl_opts = {
    'outtmpl' : os.path.join(DOWNLOAD_DIRECTORY, 'Gbot_%(title)s.%(ext)s'),
    'noplaylist' : True,
    'logger': LOGGER,
    'format': 'best',
    'geo_bypass_country': 'IN'
  }
  with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
    try:
      meta = ytdl.extract_info(link, download=True)
    except DownloadError as e:
      return False, str(e)
    for path in glob.glob(os.path.join(DOWNLOAD_DIRECTORY, '*')):
      if path.endswith(('.avi', '.mov', '.flv', '.wmv', '.3gp','.mpeg', '.webm', '.mp4', '.mkv')) and \
          path.startswith(ytdl.prepare_filename(meta)):
        return True, path
    return False, 'Something went wrong! No video file exists on server.'

def pornhub_dl(link):
  ytdl_opts = {
    'outtmpl' : os.path.join(DOWNLOAD_DIRECTORY, 'GBot_%(title)s.%(ext)s'),
    'noplaylist' : True,
    'logger': LOGGER,
    'format': 'best',
    'geo_bypass_country': 'IN'
  }
  with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
    try:
      meta = ytdl.extract_info(link, download=True)
    except DownloadError as e:
      return False, str(e)
    for path in glob.glob(os.path.join(DOWNLOAD_DIRECTORY, '*')):
      if path.endswith(('.avi', '.mov', '.flv', '.wmv', '.3gp','.mpeg', '.webm', '.mp4', '.mkv')) and \
          path.startswith(ytdl.prepare_filename(meta)):
        return True, path
    return False, 'Something went wrong! No video file exists on server.'

