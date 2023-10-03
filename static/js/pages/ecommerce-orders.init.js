function getChartColorsArray(e){var t=document.getElementById(e);if(t){t=t.dataset.colors;if(t)return JSON.parse(t).map(e=>{var t=e.replace(/\s/g,"");return t.includes(",")?2===(e=e.split(",")).length?`rgba(${getComputedStyle(document.documentElement).getPropertyValue(e[0])}, ${e[1]})`:t:getComputedStyle(document.documentElement).getPropertyValue(t)||t});console.warn("data-colors attribute not found on: "+e)}}var linechartBasicChart="";function loadCharts(){var e;(e=getChartColorsArray("line_chart_basic"))&&(e={series:[{name:"New Orders",data:[32,18,13,17,26,34,47,51,59,63,44,38,53,69,72,83,90,110,130,117,103,92,95,119,80,96,116,125]},{name:"Return Orders",data:[3,6,2,4,7,9,15,10,19,22,27,21,34,23,29,32,41,34,29,37,70,55,49,36,30,52,38,33]}],chart:{height:350,type:"line",toolbar:{show:!1}},legend:{show:!0,position:"top",horizontalAlign:"right"},grid:{yaxis:{lines:{show:!1}}},markers:{size:0,hover:{sizeOffset:4}},stroke:{curve:"smooth",width:2},colors:e,xaxis:{type:"datetime",categories:["02/01/2023 GMT","02/02/2023 GMT","02/03/2023 GMT","02/04/2023 GMT","02/05/2023 GMT","02/06/2023 GMT","02/07/2023 GMT","02/08/2023 GMT","02/09/2023 GMT","02/10/2023 GMT","02/11/2023 GMT","02/12/2023 GMT","02/13/2023 GMT","02/14/2023 GMT","02/15/2023 GMT","02/16/2023 GMT","02/17/2023 GMT","02/18/2023 GMT","02/19/2023 GMT","02/20/2023 GMT","02/21/2023 GMT","02/22/2023 GMT","02/23/2023 GMT","02/24/2023 GMT","02/25/2023 GMT","02/26/2023 GMT","02/27/2023 GMT","02/28/2023 GMT"]},yaxis:{show:!1}},""!=linechartBasicChart&&linechartBasicChart.destroy(),(linechartBasicChart=new ApexCharts(document.querySelector("#line_chart_basic"),e)).render())}window.addEventListener("resize",function(){setTimeout(()=>{loadCharts()},0)}),loadCharts();var perPage=10,editList=!1,checkAll=document.getElementById("checkAll"),options=(checkAll&&(checkAll.onclick=function(){for(var e=document.querySelectorAll('.form-check-all input[type="checkbox"]'),t=document.querySelectorAll('.form-check-all input[type="checkbox"]:checked').length,a=0;a<e.length;a++)e[a].checked=this.checked,e[a].checked?e[a].closest("tr").classList.add("table-active"):e[a].closest("tr").classList.remove("table-active"),e[a].closest("tr").classList.contains("table-active"),0<t?document.getElementById("remove-actions").classList.add("d-none"):document.getElementById("remove-actions").classList.remove("d-none")}),{valueNames:["order_id","order_date","delivery_date","products","customer","shop","payment_method","amount","rating","status"],page:perPage,pagination:!0,plugins:[ListPagination({left:2,right:2})]}),orderList=new List("orderList",options).on("updated",function(e){0==e.matchingItems.length?document.getElementsByClassName("noresult")[0].style.display="block":document.getElementsByClassName("noresult")[0].style.display="none";var t=1==e.i,a=e.i>e.matchingItems.length-e.page;document.querySelector(".pagination-prev.disabled")&&document.querySelector(".pagination-prev.disabled").classList.remove("disabled"),document.querySelector(".pagination-next.disabled")&&document.querySelector(".pagination-next.disabled").classList.remove("disabled"),t&&document.querySelector(".pagination-prev").classList.add("disabled"),a&&document.querySelector(".pagination-next").classList.add("disabled"),e.matchingItems.length<=perPage?document.querySelector(".pagination-wrap").style.display="none":document.querySelector(".pagination-wrap").style.display="flex",e.matchingItems.length==perPage&&document.querySelector(".pagination.listjs-pagination").firstElementChild.children[0].click(),0<e.matchingItems.length?document.getElementsByClassName("noresult")[0].style.display="none":document.getElementsByClassName("noresult")[0].style.display="block"}),sorttableDropdown=document.querySelectorAll(".sortble-dropdown");sorttableDropdown&&sorttableDropdown.forEach(function(a){a.querySelectorAll(".dropdown-menu .dropdown-item").forEach(function(t){t.addEventListener("click",function(){var e=t.innerHTML;a.querySelector(".dropdown-title").innerHTML=e})})});const xhttp=new XMLHttpRequest;function isStatus(e){switch(e){case"New":return'<span class="badge bg-primary-subtle text-primary">'+e+"</span>";case"Pending":return'<span class="badge bg-warning-subtle text-warning">'+e+"</span>";case"Out of Delivered":return'<span class="badge bg-danger-subtle text-danger">'+e+"</span>";case"Shipping":return'<span class="badge bg-info-subtle text-info">'+e+"</span>";case"Delivered":return'<span class="badge bg-success-subtle text-success">'+e+"</span>"}}xhttp.onload=function(){var e=JSON.parse(this.responseText);Array.from(e).forEach(function(e){orderList.add({order_id:`<a href="/apps/ecommerce/order-overview" class="fw-medium link-primary">#TBS2500${e.id}</a>`,order_date:e.order_date,delivery_date:e.delivery_date,products:e.product,customer:e.customer,shop:'<a href="#!" class="text-reset"><img src="'+e.shop[0].img+'" alt="" class="avatar-xxs rounded-circle me-1 shop-logo"> <span class="shop-name">'+e.shop[0].name+"</span></a>",payment_method:e.pay_method,amount:'<span class="fw-medium">'+e.price+"</span>",rating:'<h5 class="fs-md fw-medium mb-0">'+e.ratings+"</h5>",status:isStatus(e.delivery_status)}),orderList.sort("order_id",{order:"desc"})}),orderList.remove("order_id",'<a href="/apps/ecommerce/order-overview" class="fw-medium link-primary">#TBS250001</a>'),refreshCallbacks(),ischeckboxcheck()},xhttp.open("GET","/static/json/order-list.json"),xhttp.send(),isCount=(new DOMParser).parseFromString(orderList.items.slice(-1)[0]._values.id,"text/html"),document.querySelector(".pagination-next").addEventListener("click",function(){document.querySelector(".pagination.listjs-pagination")&&document.querySelector(".pagination.listjs-pagination").querySelector(".active")&&null!=document.querySelector(".pagination.listjs-pagination").querySelector(".active").nextElementSibling&&document.querySelector(".pagination.listjs-pagination").querySelector(".active").nextElementSibling.children[0].click()}),document.querySelector(".pagination-prev").addEventListener("click",function(){document.querySelector(".pagination.listjs-pagination")&&document.querySelector(".pagination.listjs-pagination").querySelector(".active")&&null!=document.querySelector(".pagination.listjs-pagination").querySelector(".active").previousSibling&&document.querySelector(".pagination.listjs-pagination").querySelector(".active").previousSibling.children[0].click()}),document.getElementById("showModal").addEventListener("show.bs.modal",function(e){e.relatedTarget.classList.contains("edit-item-btn")?(document.getElementById("exampleModalLabel").innerHTML="Edit Order",document.getElementById("showModal").querySelector(".modal-footer").style.display="block",document.getElementById("add-btn").innerHTML="Update"):e.relatedTarget.classList.contains("add-btn")?(document.getElementById("exampleModalLabel").innerHTML="Add Order",document.getElementById("showModal").querySelector(".modal-footer").style.display="block",document.getElementById("add-btn").innerHTML="Add Order"):(document.getElementById("exampleModalLabel").innerHTML="List product",document.getElementById("showModal").querySelector(".modal-footer").style.display="none")}),document.querySelector("#companyLogo-image-input").addEventListener("change",function(){var e=document.querySelector("#companyLogo-img"),t=document.querySelector("#companyLogo-image-input").files[0],a=new FileReader;a.addEventListener("load",function(){e.src=a.result},!1),t&&a.readAsDataURL(t)});var idField=document.getElementById("id-field"),companyLogoImg=document.getElementById("companyLogo-img"),customerNameField=document.getElementById("customername-field"),shopNameField=document.getElementById("shopName-input"),productsField=document.getElementById("productname-field"),orderDateField=document.getElementById("date-field"),amountField=document.getElementById("amount-field"),paymentField=document.getElementById("payment-field"),deliverStatsField=document.getElementById("delivered-status"),removeBtns=document.getElementsByClassName("remove-item-btn"),editBtns=document.getElementsByClassName("edit-item-btn"),productVal=new Choices(productsField,{searchEnabled:!1}),paymentVal=new Choices(paymentField,{searchEnabled:!1}),deliverStatsVal=new Choices(deliverStatsField,{searchEnabled:!1}),count=(refreshCallbacks(),13),forms=document.querySelectorAll(".tablelist-form");function ischeckboxcheck(){Array.from(document.getElementsByName("chk_child")).forEach(function(a){a.addEventListener("change",function(e){1==a.checked?e.target.closest("tr").classList.add("table-active"):e.target.closest("tr").classList.remove("table-active");var t=document.querySelectorAll('[name="chk_child"]:checked').length;e.target.closest("tr").classList.contains("table-active"),0<t?document.getElementById("remove-actions").classList.remove("d-none"):document.getElementById("remove-actions").classList.add("d-none")})})}function refreshCallbacks(){removeBtns&&Array.from(removeBtns).forEach(function(e){e.addEventListener("click",function(e){e.target.closest("tr").children[1].innerText,itemId=e.target.closest("tr").children[1].innerText;e=orderList.get({order_id:itemId});Array.from(e).forEach(function(e){var e=(new DOMParser).parseFromString(e._values.order_id,"text/html"),t=e.body.firstElementChild;e.body.firstElementChild.innerHTML==itemId&&document.getElementById("delete-record").addEventListener("click",function(){orderList.remove("order_id",t.outerHTML),document.getElementById("deleteRecord-close").click()})})})}),editBtns&&Array.from(editBtns).forEach(function(e){e.addEventListener("click",function(e){e.target.closest("tr").children[1].innerText,itemId=e.target.closest("tr").children[1].innerText;e=orderList.get({order_id:itemId});Array.from(e).forEach(function(e){var t,a=(isid=(new DOMParser).parseFromString(e._values.order_id,"text/html")).body.firstElementChild.innerHTML;a==itemId&&(editList=!0,idField.value=a,customerNameField.value=e._values.customer,productsField.value=e._values.products,paymentField.value=e._values.payment_method,a=(new DOMParser).parseFromString(e._values.status,"text/html"),deliverStatsField.value=a.body.querySelector(".badge").innerHTML,orderDateField.value=e._values.order_date,t=(new DOMParser).parseFromString(e._values.amount,"text/html"),amountField.value=t.body.querySelector("span").innerHTML,productVal&&productVal.destroy(),(productVal=new Choices(productsField,{searchEnabled:!1})).setChoiceByValue(e._values.products),t=(new DOMParser).parseFromString(e._values.shop,"text/html"),shopNameField.value=t.body.querySelector(".shop-name").innerHTML,companyLogoImg.src=t.body.querySelector(".shop-logo").src,flatpickr("#date-field",{enableTime:!0,dateFormat:"d M, Y",defaultDate:e._values.order_date}),paymentVal&&paymentVal.destroy(),(paymentVal=new Choices(paymentField,{searchEnabled:!1})).setChoiceByValue(e._values.payment_method),deliverStatsVal&&deliverStatsVal.destroy(),(deliverStatsVal=new Choices(deliverStatsField,{searchEnabled:!1})).setChoiceByValue(a.body.querySelector(".badge").innerHTML),document.getElementById("delivery-status-field").value=e._values.delivery_date,t=(new DOMParser).parseFromString(e._values.rating,"text/html"),document.getElementById("rating-field").value=t.body.querySelector("h5").innerHTML)})})})}function deleteMultiple(){ids_array=[];var e,t=document.getElementsByName("chk_child");for(i=0;i<t.length;i++)1==t[i].checked&&(e=t[i].parentNode.parentNode.parentNode.querySelector("td a").innerHTML,ids_array.push(e));"undefined"!=typeof ids_array&&0<ids_array.length?Swal.fire({title:"Are you sure?",text:"You won't be able to revert this!",icon:"warning",showCancelButton:!0,confirmButtonClass:"btn btn-primary w-xs me-2 mt-2",cancelButtonClass:"btn btn-danger w-xs mt-2",confirmButtonText:"Yes, delete it!",buttonsStyling:!1,showCloseButton:!0}).then(function(e){if(e.value){for(i=0;i<ids_array.length;i++)orderList.remove("order_id",`<a href="/apps/ecommerce/order-overview" class="fw-medium link-primary">${ids_array[i]}</a>`);document.getElementById("remove-actions").classList.add("d-none"),document.getElementById("checkAll").checked=!1,Swal.fire({title:"Deleted!",text:"Your data has been deleted.",icon:"success",confirmButtonClass:"btn btn-info w-xs mt-2",buttonsStyling:!1})}}):Swal.fire({title:"Please select at least one checkbox",confirmButtonClass:"btn btn-info",buttonsStyling:!1,showCloseButton:!0})}function clearFields(){document.getElementById("id-field").value="",companyLogoImg.src="/static/images/users/multi-user.jpg",customerNameField.value="",productsField.value="",orderDateField.value="",amountField.value="",paymentField.value="",shopNameField.value="",deliverStatsField.value="",productVal&&productVal.destroy(),productVal=new Choices(productsField,{searchEnabled:!1}),paymentVal&&paymentVal.destroy(),paymentVal=new Choices(paymentField,{searchEnabled:!1}),deliverStatsVal&&deliverStatsVal.destroy(),deliverStatsVal=new Choices(deliverStatsField,{searchEnabled:!1}),document.getElementById("companyLogo-image-input").value="",document.getElementById("delivery-status-field").value="",document.getElementById("rating-field").value=""}Array.prototype.slice.call(forms).forEach(function(e){e.addEventListener("submit",function(e){e.preventDefault();var t=document.getElementById("alert-error-msg");return t.classList.remove("d-none"),setTimeout(()=>t.classList.add("d-none"),2e3),""==customerNameField.value?!(t.innerHTML="Please enter a customer name"):""==productsField.value?!(t.innerHTML="Please select a products category"):""==orderDateField.value?!(t.innerHTML="Please select a order date"):""==shopNameField.value?!(t.innerHTML="Please enter a shop name"):""==amountField.value?!(t.innerHTML="Please enter a amount"):""==paymentField.value?!(t.innerHTML="Please select a payment method"):""==deliverStatsField.value?!(t.innerHTML="Please select a delivery status"):(""===customerNameField.value||""===productsField.value||""===orderDateField.value||""===shopNameField.value||""===amountField.value||""===paymentField.value||""===deliverStatsField.value||editList?""!==customerNameField.value&&""!==productsField.value&&""!==orderDateField.value&&""!==shopNameField.value&&""!==amountField.value&&""!==paymentField.value&&""!==deliverStatsField.value&&editList&&(e=orderList.get({order_id:idField.value}),Array.from(e).forEach(function(e){(isid=(new DOMParser).parseFromString(e._values.order_id,"text/html")).body.firstElementChild.innerHTML==itemId&&e.values({order_id:'<a href="/apps/ecommerce/order-overview" class="fw-medium link-primary">'+idField.value+"</a>",order_date:orderDateField.value,delivery_date:document.getElementById("delivery-status-field").value,products:productsField.value,customer:customerNameField.value,shop:'<a href="#!" class="text-reset"><img src="'+companyLogoImg.src+'" alt="" class="avatar-xxs rounded-circle me-1 shop-logo"> <span class="shop-name">'+shopNameField.value+"</span></a>",payment_method:paymentField.value,amount:'<span class="fw-medium">'+amountField.value+"</span>",rating:'<h5 class="fs-md fw-medium mb-0">'+document.getElementById("rating-field").value+"</h5>",status:isStatus(deliverStatsField.value)})}),document.getElementById("alert-error-msg").classList.add("d-none"),document.getElementById("close-ordermodal").click(),clearFields(),Swal.fire({position:"center",icon:"success",title:"Order updated Successfully!",showConfirmButton:!1,timer:2e3,showCloseButton:!0})):(orderList.add({order_id:'<a href="/apps/ecommerce/order-overview" class="fw-medium link-primary">#TBS2500'+count+"</a>",order_date:orderDateField.value,delivery_date:"--",products:productsField.value,customer:customerNameField.value,shop:'<a href="#!" class="text-reset"><img src="'+companyLogoImg.src+'" alt="" class="avatar-xxs rounded-circle me-1 shop-logo"> <span class="shop-name">'+shopNameField.value+"</span></a>",payment_method:paymentField.value,amount:'<span class="fw-medium">'+amountField.value+"</span>",rating:'<h5 class="fs-md fw-medium mb-0">--</h5>',status:isStatus(deliverStatsField.value)}),orderList.sort("order_id",{order:"desc"}),document.getElementById("alert-error-msg").classList.add("d-none"),document.getElementById("close-ordermodal").click(),count++,clearFields(),refreshCallbacks(),Swal.fire({position:"center",icon:"success",title:"Order inserted successfully!",showConfirmButton:!1,timer:2e3,showCloseButton:!0})),!0)})}),document.getElementById("showModal").addEventListener("hidden.bs.modal",function(){clearFields()});