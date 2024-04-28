import csv

with open("Pokemon Shows - Sheet1.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        servicename = row[0]
        servicecssclass = row[1]
        serviceiconurl = row[2]
        showname = row[3]
        showicon = row[4]
        showiconwidth = row[5]
        showiconheight = row[6]
        showseason = row[7]
        showvolume = row[8]
        paid = row[9]

        print('<div class="',"".join(servicecssclass),'">')
        print('    <div class="module">')
        print('        <div>')
        print('            <img src="',"".join(showicon),'" alt="',"".join(showname),'" width="',"".join(showiconwidth),'" height="',"".join(showiconheight),'"/>')
        print('            <div>',"".join(showname), '</div>')
        print('            <div>Season ',"".join(showseason),' Volume ',"".join(showvolume),'</div>')
        print('            <br/>')
        print('            <img src="',"".join(serviceiconurl),'" alt="',"".join(servicename),'" width="75" height="75"/>')
        print('            <div>',"".join(paid),'</div>')
        print('        </div>')
        print('    </div>')
        print('</div>')
        print('<!-- section -->')