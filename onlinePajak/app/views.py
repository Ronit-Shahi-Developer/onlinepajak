from fastparquet import ParquetFile
from rest_framework.decorators import action, api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


@api_view(['GET', 'POST'])                                              # GET and POST method
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))   # Decorator class for rendering restapi in django template
def GetVendor(request, format=None):                       # function   GetVendor
    if request.method == 'POST':                           # Checking if the request method is post
        vendor = request.POST.get('vendor')               # requesting form data and asigining in vendor
        pf = ParquetFile('test_invoices.parquet')          # paraquet file, file location
        df = pf.to_pandas()                                # converting into panda dataframe

        # Assuming that name of vendor can also be found in company.
        result = df.loc[(df['vendor_name'].str.lower() == str.lower(vendor)) |
                        (df['company_name'].str.lower() == str.lower(vendor))]


        if (result.empty):
            # if no data is found
            context = 'Third-party company ' + vendor + ' is not a user of our platforms'  #message
        else:
            # if data is found
            context = 'Third-party company ' + vendor + ' is a user of our platforms'   #message

        return Response({'context': context, 'vendor': vendor}, template_name='relationshipForm.html') # responding if the method is POST
    #else
    return Response(template_name='home.html')
#


@api_view(['GET', 'POST'])                                                # GET and POST method
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))                    # Decorator class for rendering restapi in django template
def transactionNumberView(request):                                         # function

    if request.method == 'POST':                                     # Checking if the request method is post
        vendor = request.POST.get('vendor')                        # requesting hidden form data and asigining in vendor
        company = request.POST.get('company')                  # requesting form data and asigining in company
        pf = ParquetFile('test_invoices.parquet')               # paraquet file, file location
        df = pf.to_pandas()                                        # converting into panda dataframe
        result1 = df.loc[(df['vendor_name'].str.lower() == str.lower(vendor)) &
                        (df['company_name'].str.lower() == str.lower(company))
                        ]
        # Assumming vendor can also be a company making transaction with others
        result2= df.loc[(df['vendor_name'].str.lower() == str.lower(company)) &
                        (df['company_name'].str.lower() == str.lower(vendor))
                        ]


    # total transaction with one another
    total = str(len(result1) + (len(result2)))      # totall transaction with one another

    # print(total)
    return Response({'company': company, 'total': total, 'vendor': vendor}, template_name='transactionPage.html')





