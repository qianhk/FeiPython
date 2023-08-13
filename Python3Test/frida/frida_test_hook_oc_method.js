//console.log("[*] Started: Find All Methods of a Specific Class");
//if (ObjC.available) {
//  try {
//    var className = "*AboutViewController";
//    var methods = 'ObjC.classes.' + className + '.$methods');
//    for (var i = 0; i < methods.length; i++) {
//      try {
//        console.log("[-] " + methods[i]);
//      } catch (err) {
//        console.log("[!] Exception1: " + err.message);
//      }
//    }
//  } catch (err) {
//    console.log("[!] Exception2: " + err.message);
//  }
//} else {
//  console.log("Objective-C Runtime is not available!");
//}
//console.log("[*] Completed: Find All Methods of a Specific Class");

// var className = "_TtC8Abc19AboutViewController";
// var funcName = "- setXxxxxxView:";
// console.log("before eval")
// var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
// //var hook = ObjC.classes.' + className + '["' + funcName + '"]');
// console.log("after eval")
// console.log("[*] Class Name: " + className);
// console.log("[*] Method Name: " + funcName);
// // #Interceptor.attach(target, callbacks)
// // #target是NativePointer指定要拦截调用的函数的地址
// // #如果从Frida API获取地址（例如Module.getExportByName()），Frida将处理详细信息
//
// Interceptor.attach(hook.implementation, {
//
// // #回调函数给出一个参数  args，可用于读取或写入参数作为NativePointer对象数组
//   onEnter: function(args) {
//     console.log(`-[Kai: AboutViewController setXxxxView:${args[2]}]`);
//   }, // #给定一个参数的回调函数，该参数 retval是NativePointer包含原始返回值的衍生对象
// // #请注意，此对象在onLeave调用中循环使用，因此请勿在回调之外存储和使用它。如果需要存储包含的值，请进行深层复制，例如：ptr(retval.toString())
//   onLeave: function(retval) {
//
//   }
// });

// var resolver = new ApiResolver('objc');
// // enumerateMatches() 中参数为正则表达式，格式为 *[* *]
// resolver.enumerateMatches('*[*AboutViewController *?xxxxxxView*]', {
//   onMatch: function(match) {
//     console.log(match['name'] + ":" + match['address']);
//     var method = match['name'];
//     var implementation = match['address'];
//     console.log(`kai method ${method}`);
//     if (method.indexOf(".cxx_destruct") === -1) {
//       try {
//         Interceptor.attach(ptr(implementation), {
//           onEnter: function(args) {
//             console.log("kai ======onenter=======");
//             console.log("[*] Method Name: " + method);
//             // args[0]指向类本身
//             // args[1]指向selector
//             // oc的参数从args[2]开始
//             console.log("[*] args[2]: " + args[2]);
//
//             // 实体化为oc类
//             var arg2 = new ObjC.Object(args[2]);
//             console.log(arg2.toString());
//           },
//           onLeave: function(retval) {
//             console.log("kai ======onleave=======");
//             console.log("[*] Method Name: " + method);
//             console.log("\t[-] retval: " + retval);
//           }
//         });
//       } catch (err) {
//         console.log("kai [!] Exception: " + err.message);
//       }
//     }
//   },
//   onComplete: function() {
//   }
// });


var resolver = new ApiResolver('objc');
// enumerateMatches() 中参数为正则表达式，格式为 *[* *]
resolver.enumerateMatches('*[*?xxxxx* *]', {
  onMatch: function(match) {
    console.log(match['name'] + ":" + match['address']);
    var method = match['name'];
    var implementation = match['address'];

    if (method.indexOf("XxxApp") >= 0 && method.indexOf(".cxx_destruct") === -1) {
      try {
        Interceptor.attach(ptr(implementation), {
          onEnter: function(args) {
            console.log("kai1 ======onenter=======");
            console.log("[*] Method Name: " + method);
            // args[0]指向类本身
            // args[1]指向selector
            // oc的参数从args[2]开始
            console.log("[*] args[2]: " + args[2]);

            // 实体化为oc类
            var arg2 = new ObjC.Object(args[2]);
            console.log(arg2.toString());
          },
          onLeave: function(retval) {
            console.log("kai1 ======onleave=======");
            console.log("[*] Method Name: " + method);
            console.log("\t[-] retval: " + retval);
          }
        });
      } catch (err) {
        console.log("kai [!] Exception: " + err.message);
      }
    }
  },
  onComplete: function() {
  }
});

resolver.enumerateMatches('*[* *?xxxxx*]', {
  onMatch: function(match) {
    console.log(match['name'] + ":" + match['address']);
    var method = match['name'];
    var implementation = match['address'];

    if (method.indexOf("XxxApp") >= 0 && method.indexOf(".cxx_destruct") === -1) {
      try {
        Interceptor.attach(ptr(implementation), {
          onEnter: function(args) {
            console.log("kai2 ======onenter=======");
            console.log("[*] Method Name: " + method);
            // args[0]指向类本身
            // args[1]指向selector
            // oc的参数从args[2]开始
            console.log("[*] args[2]: " + args[2]);

            // 实体化为oc类
            var arg2 = new ObjC.Object(args[2]);
            console.log(arg2.toString());
          },
          onLeave: function(retval) {
            console.log("kai2 ======onleave=======");
            console.log("[*] Method Name: " + method);
            console.log("\t[-] retval: " + retval);
          }
        });
      } catch (err) {
        console.log("kai [!] Exception: " + err.message);
      }
    }
  },
  onComplete: function() {
  }
});


