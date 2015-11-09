$(document).ready(function() {
  $('#sidr-button').sidr({
  	onOpen : function() {
			$('.sidr-overlay').show();
		}
  });

  $('body').on('click', '.sidr-overlay', function(){
		$.sidr('close', 'sidr');
		$(this).hide();
	});
});

//Charts
var pieData = new Array();

    $(document).ready(function () {
		
		function piechart(pieData){
			//console.log(pieData);
			new Highcharts.Chart({
	            chart: {
	            	renderTo: pieData.renderTo,
	                plotBackgroundColor: null,
	                plotBorderWidth: null,
	                plotShadow: false,
	                inverted: true,
	                type: 'pie',
	                height: 120,
	                spacing:[0,0,0,0],

	            },
	            title: {                
	                text: "",
	            },
	            tooltip: {
	            	enabled: false,                
	            },
	            exporting: { enabled: false },
	            plotOptions: {
	                pie: {                                        
	                    dataLabels: {
	                        enabled: false
	                    },
	                    showInLegend: true,
	                    enableMouseTracking: false,
	                }
	            },
	            legend:{
	            	enabled: false,
	            	labelFormatter: function () {
	                	return this.name + " " + this.percentage.toFixed(0) + '%';
	            	}
	            },
	            series: [{
	                name: "Brands",
	                colorByPoint: true,
	                data: pieData.data,
	            }]
	        });			

		}
		    
		

		
        // Build the chart
        $('.piechart').each(function(index){			
        	parent = $(this).parent().parent().parent().parent();
    		pieData[index] = {
	    			renderTo : $(this).attr("id"),
	    			data :[{	
	                    name: "Apoyan",
	                    y: $(this).attr("data-yes") * 100 / (parseInt($(this).attr("data-yes")) + parseInt($(this).attr("data-no"))),
	                    color: parent.attr("is-backer") == 1 ? "#3B5998" : "#ccc",	                    
	                }, {
	                    name: "No Apoyan",
	                    y: $(this).attr("data-no") * 100 / (parseInt($(this).attr("data-yes")) + parseInt($(this).attr("data-no"))),
	                    color: parent.attr("is-backer") == 0 ? "#3B5998" : "#ccc",	                    
	                }]
            };
        	if(parent.attr("is-backer")==0){
        		pieData[index].data.reverse();	
            }            
	   		
	    });

        if(pieData.length > 0){
			piechart(pieData[0]); //Without this, the first one always misses
	        for(i=0;i < pieData.length;i++){                	
	        	console.log(pieData[0]);
	        	piechart(pieData[i]);	
	        }
    	}  
    });
