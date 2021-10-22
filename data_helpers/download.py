import requests
import tqdm


def download(url, output_dir, filename=None, skip_if_exists=True):
    """
    Download a file from a URL and save in a local directory
    
    Returns the path to the downloaded file
    
    This is based on the snippet in
    https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests
    
    """
    if filename is None:
        filename = urlparse(url).path.split("/")[-1]
        
    output_path = Path(output_dir) / filename
    
    # Decide if we're actually going to download the file
    do_download = (
        # If `skip_if_exists` is False, we should download
        (not skip_if_exists)
        # If the file doesn't exist, we should download 
        or (not output_path.exists())
    )
    
    if not do_download:
        if output_path.exists():
            logging.info("Skipping download because `%s` already exists", output_path)
            
        # If not downloading the file, return early
        return output_path
    
    resp = requests.get(url, stream=True, allow_redirects=True)
    
    if resp.status_code != 200:
        resp.raise_for_status()
        
    # TODO: Decide if this should default to zero or raise an exception
    file_size = int(resp.headers.get("Content-Length", 0))
    
    block_size = 1024 # 1024 bytes in one KB
    
    # This seems cleaner, but it doesn't get the units right
    #progress_bar = tqdm(resp.iter_content(block_size), total=file_size // block_size, unit="iB", unit_scale=True)
    # So, instead of doing `for data in progress_bar`, we'll iterate
    # through `resp.iter_content(block_size) and manually update the bar.
    progress_bar = tqdm(total=file_size, unit="iB", unit_scale=True)
    
    with open(output_path, "wb") as outf:
        for data in resp.iter_content(block_size):
            progress_bar.update(len(data))
            outf.write(data)
    
    progress_bar.close()
    
    return output_path
