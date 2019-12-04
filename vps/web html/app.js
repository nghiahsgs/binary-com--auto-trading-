console.log('hello')
var ws = new WebSocket('wss://ws.binaryws.com/websockets/v3?app_id=20922');

ws.onopen = function(evt) {
    ws.send(JSON.stringify({ticks:'frxEURUSD'}));
};
// nbs_price=5*60 //5 min, moi min co 60s
min_price_5minute=1000 //gia tri bt cua EUR/USD 1.1, cho han 1000 cho to
max_price_5minute=0  // initial value =0
open_price_5minute=0
close_price_5minute=0
ws.onmessage = function(msg) {
	//1s chay ham nay 1 lan
   var data = JSON.parse(msg.data);
   // console.log('ticks update: %o', data);
   epoch=parseInt(data['tick']['epoch'])
   // console.log(data['tick']['epoch'])
   average_price=parseFloat(data['tick']['ask'])+parseFloat(data['tick']['ask'])
   average_price=average_price/2
   // console.log(average_price)

   //tim max value during 5min
   if(average_price>max_price_5minute){
   	max_price_5minute=average_price
   }
   //tim min value during 5min
   if(average_price<min_price_5minute){
   	min_price_5minute=average_price
   }

   let date=new Date(epoch*1000)
   current_min=date.getMinutes()
   current_sec=date.getSeconds()
   // console.log('epoch',epoch)
   // console.log('current_sec',current_sec)
   /*
   if(current_min===0&&current_sec==0){
   	//if(current_sec==0){
	open_price_5minute=average_price
   }
   if(current_min===5&&current_sec==0){
	close_price_5minute=average_price
	//save value
	console.log('0min -> 5min');
	console.log('open_price_5minute',open_price_5minute)
	console.log('close_price_5minute',close_price_5minute)
	console.log('min_price_5minute',min_price_5minute)
	console.log('max_price_5minute',max_price_5minute)
	
	//reset value
	min_price_5minute=1000
	max_price_5minute=0
	open_price_5minute=average_price
	close_price_5minute=0
   }
   */
   // if(current_min%5==0&&current_sec==0){ //nen 5 phut
   if(current_min%5==0&&current_sec==0){ //nen 1 phut
	close_price_5minute=average_price
	//save value
	console.log('current_min',current_min);
	console.log(`from ${current_min-5} min to ${current_min}`);
	console.log('open_price_5minute',open_price_5minute)
	console.log('close_price_5minute',close_price_5minute)
	console.log('min_price_5minute',min_price_5minute)
	console.log('max_price_5minute',max_price_5minute)
	insertsDB(epoch,open_price_5minute,close_price_5minute,min_price_5minute,max_price_5minute)
	//reset value
	min_price_5minute=1000
	max_price_5minute=0
	open_price_5minute=average_price
	close_price_5minute=0
   }

};

function insertsDB(timestamp_start,open,close,min,max) {

	let urlInsert=`http://localhost/binary%20com%20auto%20trade/insert.php?start=${timestamp_start}&open=${open}&close=${close}&min=${min}&max=${max}`
	
	$.get(urlInsert, function(data){
		console.log(data)
	});
}