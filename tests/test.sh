for i in {4,64};do
  for j in {randread,randwrite,randrw};do
      ret=$(fio -thread  -runtime=30 -group_reporting -bs=${i}K -direct=1 -rw=${j} -ioengine=psync -numjobs=48 -iodepth=1 -name=fiotest01 -filename=/dev/sda)
      echo "/dev/sda ${i}k ${j}"
      if [[ "${j}" == "randread" ]];then
          bw=$(awk '/read:/ {print($3)}' <<<"${ret}")
          iops=$(awk '/read:/ {print($2)}' <<<"${ret}" | tr -d ',')
          lat=$(awk -F '=' '/clat \(usec\):/ {print($5)}' <<<"${ret}" | tr -d 'stdev' | tr -d ',')
          echo "${bw} ${iops} ${lat}"
      elif [[ "${j}" == "randwrite" ]];then
          bw=$(awk '/write:/ {print($3)}' <<<"${ret}")
          iops=$(awk '/write:/ {print($2)}' <<<"${ret}" | tr -d ',')
          lat=$(awk -F '=' '/clat \(usec\):/ {print($5)}' <<<"${ret}" | tr -d 'stdev' | tr -d ',')
          echo "${bw} ${iops} ${lat}"
      elif [[ "${j}" == "randrw" ]];then
          bw=$(awk '/BW=/{print($3)}' <<<"${ret}" | cut -d '=' -f 2 | tr '\n' ' ')
          iops=$(awk '/BW=/{print($2)}' <<<"${ret}" | cut -d '=' -f 2 | tr -d ',' | tr  '\n' ' ')
          lat=$(awk -F '=' '/clat \(usec\):/ {print($5)}' <<<"${ret}" | tr -d 'stdev' | tr -d ',' | tr  '\n' ' ')
          echo "BW=${bw} IOPS=${iops} ${lat}"
      fi
      echo
    done
done
for i in {0..9};do
  for j in {4,64};do
    for k in {randread,randwrite,randrw};do
        ret=$(fio -thread  -runtime=30 -group_reporting -bs=${j}K -direct=1 -rw=${k} -ioengine=psync -numjobs=48 -iodepth=1 -name=fiotest01 -filename=/dev/nvme${i}n1)
        echo "/dev/nvme${i}n1 ${j}k ${k}"
        if [[ "${k}" == "randread" ]];then
            bw=$(awk '/read:/ {print($3)}' <<<"${ret}")
            iops=$(awk '/read:/ {print($2)}' <<<"${ret}" | tr -d ',')
            lat=$(awk -F '=' '/clat \(usec\):/ {print($5)}' <<<"${ret}" | tr -d 'stdev' | tr -d ',')
            echo "${bw} ${iops} ${lat}"
        elif [[ "${k}" == "randwrite" ]];then
            bw=$(awk '/write:/ {print($3)}' <<<"${ret}")
            iops=$(awk '/write:/ {print($2)}' <<<"${ret}" | tr -d ',')
            lat=$(awk -F '=' '/clat \(usec\):/ {print($5)}' <<<"${ret}" | tr -d 'stdev' | tr -d ',')
            echo "${bw} ${iops} ${lat}"
        elif [[ "${k}" == "randrw" ]];then
            bw=$(awk '/BW=/{print($3)}' <<<"${ret}" | cut -d '=' -f 2 | tr '\n' ' ')
            iops=$(awk '/BW=/{print($2)}' <<<"${ret}" | cut -d '=' -f 2 | tr -d ',' | tr  '\n' ' ')
            lat=$(awk -F '=' '/clat \(usec\):/ {print($5)}' <<<"${ret}" | tr -d 'stdev' | tr -d ',' | tr  '\n' ' ')
            echo "BW=${bw} IOPS=${iops} ${lat}"
        fi
        echo
      done
  done
done
