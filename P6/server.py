import http.client
import http.server
import socketserver
import json
from P6.seq import Seq

socketserver.TCPServer.allow_reuse_address = True

# -- API information
HOSTNAME = "rest.ensembl.org"
METHOD = "GET"
ENDPOINT = ""
CONTENT_TYPE = "?content-type=application/json"

PORT = 8000


def connection(ENDPOINT):
    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}
    # -- Connect to the server
    conn = http.client.HTTPSConnection(HOSTNAME)
    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT + CONTENT_TYPE, None, headers)
    # -- Wait for the server's response
    r1 = conn.getresponse()
    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)
    # -- Read the response's body and close the connection
    text_json = r1.read().decode("utf-8")
    conn.close()
    # -- Create a variable with the data from the JSON received
    json_object = json.loads(text_json)
    return json_object


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("Path:", self.path)
        # If the client requests the "/" endpoint open the main page
        if self.path == "/":
            resp_code = 200
            f = open("main.html", 'r')
            contents = f.read()
            content_type = 'text/html'
# --1   If the client requests the list of species
        elif self.path == "/listSpecies":
            resp_code = 200
            # List of each specie a dictionary
            species = connection("/info/species")['species']
            n_species = len(species)
            l_species = "<ul>"
            #crating a loop for each specie
            for specie in species:
                name = specie['display_name']
                l_species += "<li>" + name + "</li>"
            html1 = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Species</title>
            </head>
            <body>"""
            html2 = "<p><b>Number of species:</b> {}</p>".format(n_species)
            html3 = "<p><b>List of all the species:</b> {}</p></body></html>".format(l_species)
            f = open("listSpecies.html", 'w')
            f.write(html1 + html2 + html3)
            f.close()
            f = open("listSpecies.html")
            contents = f.read()
            content_type = 'text/html'

# --a   If the client requests the list of species with a limit
        elif self.path.startswith("/listSpecies?limit="):
            try:
                resp_code = 200
                i = self.path.find("limit=") + len("limit=")
                limit = self.path[i:]
                # -- List of species with a limit (each specie is a dictionary)
                species = connection("/info/species")['species']
                n_species = len(species)
                if int(limit) > n_species:
                    limit = n_species
                elif int(limit) < 0:
                    limit = "a"
                l_species = "<ul>"
                for n, specie in enumerate(species):
                    if limit == "0":
                        break
                    if n != 0 and n == int(limit):
                        break
                    name = specie['display_name']
                    l_species += "<li>" + name + "</li>"
                html1 = """<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Species</title>
                </head>
                <body>"""
                html2 = "<p><b>Number of species:</b> {}</p>".format(limit)
                html3 = "<p><b>List of the species:</b> {}</p></body></html>".format(l_species)
                f = open("listSpecies.html", 'w')
                f.write(html1 + html2 + html3)
                f.close()
                f = open("listSpecies.html")
                contents = f.read()
                content_type = 'text/html'
            # If the limit is not correct
            except IndexError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                content_type = 'text/html'
            # If the limit is not a number
            except ValueError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                content_type = 'text/html'

# --2   If the user requests the Karyotype
        elif self.path.startswith("/karyotype"):
            resp_code = 200
            i = self.path.find("specie=") + len("specie=")
            specie_name = self.path[i:]
            if "+" in specie_name:
                specie_name = specie_name.replace("+", "_")
            try:
                # List with the name of the chromosomes
                karyotype = connection("/info/assembly/" + specie_name)['karyotype']
                l_chrom = "<ul>"
                for n, chrom in enumerate(karyotype):
                    l_chrom += "<li>" + chrom + "</li>"
                html1 = """<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Karyotype</title>
                </head>
                <body>"""
                html2 = "<p><b>List of the karyotype of the specie {}:</b> {}</p>".format(specie_name, l_chrom)
                html3 = "</body></html>"
                f = open("karyotype.html", 'w')
                f.write(html1 + html2 + html3)
                f.close()
                f = open("karyotype.html")
                contents = f.read()
                content_type = 'text/html'
            # If the name of the specie is not found
            except KeyError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                content_type = 'text/html'

# --3   If the user requests the chromosome length
        elif self.path.startswith("/chromosomeLength"):
            resp_code = 200
            i = self.path.find("specie=") + len("specie=")
            j = self.path.find("chromo=") + len("chromo=")
            specie_name = self.path[i:self.path.find("&")]
            chrom_name = self.path[j:]
            if "+" in specie_name:
                specie_name = specie_name.replace("+", "_")
            try:
                loop = True
                length_chrom = ''
                # List with dictionaries that contain the name and length of the chromosomes
                length_chrom = connection("/info/assembly/" + specie_name)['top_level_region']
                for dicti in length_chrom:
                    n_chromosome = dicti['name']
                    if n_chromosome == chrom_name:
                        length_chrom = dicti['length']
                        loop = False
                        break
                if loop is True:
                    f = open("error_parameter.html", 'r')
                    contents = f.read()
                    content_type = 'text/html'
                else:
                    html1 = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Chromosome length</title>
                    </head>
                    <body>"""
                    html2 = "<p><b>Length of the chromosome {}".format(chrom_name)
                    html3 = " of the specie {}:</b> {}</p>".format(specie_name, length_chrom)
                    html4 = "</body></html>"
                    f = open("chromosomeLength.html", 'w')
                    f.write(html1 + html2 + html3 + html4)
                    f.close()
                    f = open("chromosomeLength.html")
                    contents = f.read()
                    content_type = 'text/html'
            # If the name of the chromosome is not found
            except UnboundLocalError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                content_type = 'text/html'
            # If the specie is not found
            except KeyError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                content_type = 'text/html'
# -- MEDIUM LEVEL
# --4   If the user requests the sequence of a gene
        elif self.path.startswith("/geneSeq"):
            try:
                resp_code = 200
                x = self.path.find("gene=") + len("gene=")
                gene = self.path[x:]
                id_gene = connection("/homology/symbol/human/" + gene)['data'][0]['id']
                gene_seq = connection("sequence/id/" + id_gene)['seq']
                html1 = """<!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <title>Sequence of a gene</title>
                </head>
                <body>"""
                html2 = "<p><b>Sequence of the gene {}:</b> {}</p>".format(gene, gene_seq)
                html3 = "</body></html>"
                f = open("geneSeq.html", 'w')
                f.write(html1 + html2 + html3)
                f.close()
                f = open("geneSeq.html")
                contents = f.read()
                content_type = 'text/html'
            # If the gene is wrong or not found
            except KeyError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                content_type = 'text/html'
# --5
        elif self.path.startswith("/geneInfo"):
            try:
                resp_code = 200
                x = self.path.find("gene=") + len("gene=")
                gene = self.path[x:]
                id_gene = connection("/homology/symbol/human/" + gene)['data'][0]['id']
                gene_seq = connection("/sequence/id/" + id_gene)['seq']
                info_gene = connection("/lookup/id/" + id_gene)
                chrom = info_gene['seq_region_name']
                end = info_gene['end']
                start = info_gene['start']
                gene_seq = Seq(gene_seq)
                length_seq = gene_seq.len()
                html1 = """<!DOCTYPE html>
                <html lang="en">
                <head>
                <meta charset="UTF-8">
                <title>Gene information</title>
                </head>
                <body>"""
                html2 = "<p><b>Start of the gene:</b> {}".format(start)
                html3 = "<br><b>End of the gene:</b> {}".format(end)
                html4 = "<br><b>Length of the gene:</b> {}".format(length_seq)
                html5 = "<br><b>Id of the gene:</b> {}".format(id_gene)
                html6 = "<br><b>Chromosome that contains the gene:</b> {}".format(chrom)
                html7 = "</body></html>"
                f = open("geneSeq.html", 'w')
                f.write(html1 + html2 + html3 + html4 + html5 + html6 + html7)
                f.close()
                f = open("geneSeq.html")
                contents = f.read()
                content_type = 'text/html'
            # If the gene is wrong or not found
            except KeyError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                content_type = 'text/html'

# --6   If the user requests calculations on the sequence of a gene
        elif self.path.startswith("/geneCal"):
            try:
                resp_code = 200
                x = self.path.find("gene=") + len("gene=")
                gene = self.path[x:]
                id_gene = connection("/homology/symbol/human/" + gene)['data'][0]['id']
                gene_seq = connection("/sequence/id/" + id_gene)['seq']
                gene_seq = Seq(gene_seq)
                length_seq = gene_seq.len()
                perc_print = ""
                for base in 'ACGT':
                    perc = gene_seq.perc(base)
                    perc_print += "<br>The percentage of the base {} is: {}% <br>".format(base, perc)
                html1 = """<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Calculations on sequence of a gene</title>
                </head>
                <body>"""
                html2 = "<b>Total length of the sequence of the gene {}:</b> {}".format(gene, length_seq)
                html3 = "<p>{}</p></body></html>".format(perc_print)
                f = open("geneCal.html", 'w')
                f.write(html1 + html2 + html3)
                f.close()
                f = open("geneCal.html")
                contents = f.read()
                content_type = 'text/html'
            # If the gene is wrong or not found
            except KeyError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                content_type = 'text/html'

# --7   # If the user requests names of the genes located in the chromosome "chromo" from the start to end positions
        elif self.path.startswith("/geneList"):
            try:
                resp_code = 200
                i = self.path.find("start=") + len("start=")
                j = self.path.find("&end")
                region_start = self.path[i:j]
                x = self.path.find("end=") + len("end=")
                region_end = self.path[x:]
                region = region_start + "-" + region_end
                n = self.path.find("chromo=") + len("chromo=")
                m = self.path.find("&start")
                chrom = self.path[n:m]
                ENDPOINT = "/overlap/region/human/" + str(chrom) + ":" + str(region)
                CONTENT_TYPE = "?content-type=application/json;feature=gene;feature=transcript;feature=cds;feature=exon"
                # info = connection("/overlap/region/human/" + str(chrom) + ":" + str(region))
                headers = {'User-Agent': 'http-client'}
                conn = http.client.HTTPSConnection(HOSTNAME)
                conn.request(METHOD, ENDPOINT + CONTENT_TYPE, None, headers)
                r1 = conn.getresponse()
                print()
                print("Response received: ", end='')
                print(r1.status, r1.reason)
                # -- Read the response's body and close the connection
                text_json = r1.read().decode("utf-8")
                conn.close()
                # -- Create a variable with the data from the JSON received
                json_object = json.loads(text_json)
                l_genes = "<ul>"
                for gene in json_object:
                    type_gene = gene['feature_type']
                    if type_gene == "gene":
                        gene_id = gene['id']
                        l_genes += "<li>" + gene_id + "</li>"
                    else:
                        pass
                html1 = """<!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Names of the genes</title>
                    </head>
                    <body>"""
                html2 = "<p><b>Start:</b> {}</p><p><b>End:</b> {}</p>".format(region_start, region_end)
                html3 = "<p><b>Chromosome:</b> {}</p>".format(chrom)
                html4 = "<p><b>List of genes:</b> {}</p></body></html>".format(l_genes)
                f = open("geneList.html", 'w')
                f.write(html1 + html2 + html3 + html4)
                f.close()
                f = open("geneList.html")
                contents = f.read()
                content_type = 'text/html'
            # If the gene is wrong or not found
            except KeyError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                f.close()
                content_type = 'text/html'
            except TypeError:
                resp_code = 404
                f = open("error_parameter.html", 'r')
                contents = f.read()
                f.close()
                content_type = 'text/html'
# If the resource requested from the client is incorrect, send an error message
        else:
            resp_code = 404
            f = open("error.html", 'r')
            contents = f.read()
            content_type = 'text/html'

        # Sending the response to the client
        self.send_response(resp_code)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        # Sending the body of the response message
        self.wfile.write(str.encode(contents))
        return


# -- Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT: {}".format(PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("Stopped by the user")
print("The server is stopped")



