'use strict';

const chess = require('chess');

const wrapper = require('./chesswrapper.js')
module.exports.hello = async event => {

  const gameClient = chess.create();
  let move, status;

  status = gameClient.getStatus();
  wrapper.initiateGame();
  wrapper.makeMove('a4');
  wrapper.makeMove('h6');

  wrapper.makeMove('a5');
  wrapper.makeMove('b5');
  return wrapper.makeMove('b6');
/*  wrapper.makeMove('c4');
  wrapper.makeMove('c6');

  wrapper.makeMove('d4');
  wrapper.makeMove('d6');

  wrapper.makeMove('e4');
  wrapper.makeMove('e6');

  wrapper.makeMove('Na3');
  wrapper.makeMove('f6');

  wrapper.makeMove('Bb2');
  wrapper.makeMove('g6');

  wrapper.makeMove('Qd2');
  wrapper.makeMove('h6');

  wrapper.makeMove('Rb1');*/
  //wrapper.makeMove('a4');
  return wrapper.getStatus().notatedMoves;


  // Use this code if you don't use the http event with the LAMBDA-PROXY integration
  // return { message: 'Go Serverless v1.0! Your function executed successfully!', event };
};
