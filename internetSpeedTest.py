# Install_library
# pip install speedtest-cli

import speedtest as st

server = st.Speedtest()
server.get_best_server()

# Test download server
down =server.download()
down = down / 1000000
# Test upload server
up = server.upload()
up = up / 1000000
# Test ping
ping = server.results.ping
# print results
print('===  RESULTS  ===')
print(f"Download Speed: {down}  Mb/s")
print(f"Upload Speed: {up}  Mb/s")
print(f"Ping Speed: {ping}  Mb/s")
