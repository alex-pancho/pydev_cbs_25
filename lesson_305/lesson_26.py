# import requests
# import functools
# import time


# def get_duration(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         duration = time.time() - start_time
#         print(f"Duration = {duration}")
#         return res

#     return wrapper


# def download_site(url, session, count):
#     with session.get(url) as response:
#         print(f"{count} --> Read {len(response.content)} from {url}")


# @get_duration
# def download_all_sites(sites):
#     with requests.Session() as session:
#         for count, url in enumerate(sites):
#             download_site(url, session, count)


# sites = [
#             "http://www.testingmcafeesites.com/index.html",
#             "https://www.jython.org"
#         ] * 200

# download_all_sites(sites)

# import concurrent.futures
# import requests
# import threading
# import time
# import functools

# thread_local = threading.local()


# def get_duration(func):
#     @functools.wraps(func)
#     def wraper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         duration = time.time() - start_time
#         print(f"Duration = {duration}")
#         return res

#     return wraper


# def get_session():
#     if not hasattr(thread_local, "session"):
#         thread_local.session = requests.Session()
#     return thread_local.session


# def download_site(site_num):
#     session = get_session()
#     with session.get(site_num[1]) as response:
#         print(f"{site_num[0]}: read {len(response.content)} from {site_num[1]}")


# @get_duration
# def download_all_sites(sites):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
#         executor.map(download_site, sites)


# sites = [
#             "http://www.testingmcafeesites.com/index.html",
#             "https://www.jython.org"
#         ] * 200

# sites_num = [(num, site) for num, site in enumerate(sites)]
# download_all_sites(sites_num)

# import asyncio
# import time
# import aiohttp
# import functools
# import sys
# import inspect


# def get_duration(func):
#     """
#     Works for both regular and async functions.
#     """
#     if inspect.iscoroutinefunction(func):
#         @functools.wraps(func)
#         async def async_wrapper(*args, **kwargs):
#             start_time = time.time()
#             res = await func(*args, **kwargs)
#             duration = time.time() - start_time
#             print(f"Duration = {duration:.3f} sec")
#             return res
#         return async_wrapper
#     else:
#         @functools.wraps(func)
#         def sync_wrapper(*args, **kwargs):
#             start_time = time.time()
#             res = func(*args, **kwargs)
#             duration = time.time() - start_time
#             print(f"Duration = {duration:.3f} sec")
#             return res
#         return sync_wrapper


# async def download_site(session: aiohttp.ClientSession, url: str, num: int, sem: asyncio.Semaphore = None):
#     """
#     Download a single URL. If sem is provided, it will limit concurrency.
#     Returns tuple (num, url, size, status, error)
#     """
#     if sem is None:
#         acquire = asyncio.sleep(0, result=None)  # no-op awaitable
#     else:
#         acquire = sem.acquire()

#     await acquire
#     try:
#         # small per-request timeout
#         timeout = aiohttp.ClientTimeout(total=15)
#         async with session.get(url, timeout=timeout) as response:
#             body = await response.read()
#             size = len(body)
#             print(f"Read -{num}- {size} bytes from {url}, status {response.status}")
#             return (num, url, size, response.status, None)
#     except Exception as e:
#         print(f"Error -{num}- downloading {url}: {e}")
#         return (num, url, None, None, e)
#     finally:
#         if sem is not None:
#             sem.release()


# @get_duration
# async def download_all_sites(sites, max_connections=100, use_semaphore=False):
#     """
#     Download all sites concurrently.
#     - max_connections controls aiohttp.TCPConnector(limit=...)
#     - set use_semaphore=True to enforce a semaphore in addition to connector limit
#     """
#     connector = aiohttp.TCPConnector(limit=max_connections, force_close=False)
#     # You may set trust_env=True if you need system proxies
#     timeout = aiohttp.ClientTimeout(total=None)  # per-request timeouts are set in download_site
#     sem = asyncio.Semaphore(max_connections) if use_semaphore else None

#     async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
#         tasks = [
#             asyncio.create_task(download_site(session, url, num, sem))
#             for num, url in enumerate(sites)
#         ]
#         results = await asyncio.gather(*tasks, return_exceptions=False)
#     return results


# def prepare_sites():
#     return [
#         "http://www.testingmcafeesites.com/index.html",
#         "https://www.jython.org",
#     ] * 200


# def main():
#     # On Windows, some Python versions need selector event loop for aiohttp
#     if sys.platform.startswith("win"):
#         try:
#             # This call is safe on non-Windows too, but it's only necessary on Windows
#             asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#         except Exception:
#             pass

#     sites = prepare_sites()
#     start_time = time.time()
#     # Tune max_connections according to your environment
#     results = asyncio.run(download_all_sites(sites, max_connections=100, use_semaphore=False))
#     duration = time.time() - start_time
#     success = sum(1 for r in results if r[2] is not None)
#     print(f"Total duration = {duration:.3f} sec. Successful: {success}/{len(results)}")


# if __name__ == "__main__":
#     main()


# import requests
# import multiprocessing
# import time
# import functools
# import sys

# session = None


# def get_duration(func):
#     @functools.wraps(func)
#     def wraper(*args, **kwargs):
#         start_time = time.time()
#         res = func(*args, **kwargs)
#         duration = time.time() - start_time
#         print(f"Duration = {duration}")
#         return res

#     return wraper


# def set_global_session():
#     global session
#     if not session:
#         session = requests.Session()


# def download_site(url):
#     with session.get(url) as response:
#         name = multiprocessing.current_process().name
#         print(f"{name}:Read {len(response.content)} from {url}")


# def download_site(url, timeout=15):
#     """
#     Download a single URL using the process-local `session`.
#     Returns (process_name, url, size or None, status or None, error or None)
#     """
#     global session
#     name = multiprocessing.current_process().name
#     if session is None:
#         # Defensive: if session wasn't initialized for any reason, create one here
#         set_global_session()

#     try:
#         resp = session.get(url, timeout=timeout)
#         resp.raise_for_status()
#         size = len(resp.content)
#         print(f"{name}: Read {size} bytes from {url}")
#         return (name, url, size, resp.status_code, None)
#     except requests.RequestException as e:
#         print(f"{name}: Error downloading {url} -> {e}")
#         return (name, url, None, None, e)


# @get_duration
# def download_all_sites(sites, processes=None, chunksize=1):
#     """
#     Download all sites using a multiprocessing.Pool.
#     - processes: number of worker processes (None => cpu_count())
#     - chunksize: controls how tasks are split (increase for many small tasks)
#     Returns list of results from workers.
#     """
#     # Use default number of processes if not specified
#     if processes is None:
#         processes = multiprocessing.cpu_count()

#     with multiprocessing.Pool(processes=processes, initializer=set_global_session) as pool:
#         # pool.map will wait for completion and collect results
#         results = pool.map(download_site, sites, chunksize)
#     return results


# if __name__ == "__main__":
#     # Required on Windows to start child processes safely
#     multiprocessing.freeze_support()

#     sites = [
#         "http://www.testingmcafeesites.com/index.html",
#         "https://www.jython.org",
#     ] * 200

#     start = time.time()
#     results = download_all_sites(sites, processes=8, chunksize=4)  # tune processes/chunksize as needed
#     total_time = time.time() - start

#     success_count = sum(1 for r in results if r[2] is not None)
#     print(f"Total duration = {total_time:.3f} sec. Successful: {success_count}/{len(results)}")


import requests
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor

# Global (process-local) session
session = None


def set_global_session():
    """
    Initializer for each process in the pool.
    Creates a session unique to this process.
    """
    global session
    if session is None:
        s = requests.Session()
        s.headers.update({"User-Agent": "mp-thread-downloader/1.0"})
        session = s


def download_one(url):
    """
    Executed inside a thread.
    Uses the process-level session.
    """
    global session
    try:
        resp = session.get(url, timeout=10)
        resp.raise_for_status()
        size = len(resp.content)
        pname = multiprocessing.current_process().name
        print(f"{pname}: Thread read {size} bytes from {url}")
        return (url, size, None)
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return (url, None, e)


def download_with_threads(urls, threads_per_process=10):
    """
    Executed inside **each process**.
    Starts a thread pool and downloads URLs assigned to this process.
    """
    with ThreadPoolExecutor(max_workers=threads_per_process) as executor:
        results = list(executor.map(download_one, urls))
    return results


def chunkify(data, n_chunks):
    """Split list into n roughly equal chunks."""
    k, m = divmod(len(data), n_chunks)
    return [data[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n_chunks)]


def download_all(sites, processes=4, threads=20):
    """
    Split URLs across processes, each process runs ThreadPoolExecutor.
    """
    chunks = chunkify(sites, processes)

    with multiprocessing.Pool(processes=processes, initializer=set_global_session) as pool:
        results = pool.starmap(
            download_with_threads,
            [(chunk, threads) for chunk in chunks]
        )

    # Flatten and return
    return [item for sublist in results for item in sublist]


if __name__ == "__main__":
    multiprocessing.freeze_support()

    sites = [
        "http://www.testingmcafeesites.com/index.html",
        "https://www.jython.org",
    ] * 200  # 400 URLs total

    start = time.time()

    results = download_all(
        sites,
        processes=4,      # number of Python processes
        threads=20,       # threads per process
    )

    success = sum(1 for _, size, err in results if size is not None)
    duration = time.time() - start

    print(f"\nSuccessful: {success}/{len(results)}")
    print(f"Total Duration: {duration:.3f} sec")