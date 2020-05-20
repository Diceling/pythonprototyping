'use strict';

const chess = require('chess');
var gameClient = "";
var castlings = 'KQkq';
var enPassant = '-';
var madeMoves = []
module.exports = {

initiateGame: function() {
  gameClient = chess.create();
  return "Game initiated";
},
makeMove: function(moveNot) {
  var move = gameClient.move(moveNot);
  module.exports.determineCastlings(move.move);
  madeMoves.push(moveNot);
  return move;

},
getStatus: function() {

  return gameClient.getStatus();
},

getFen: function() {
  var status = gameClient.getStatus();

  var squares = status.board.squares;
  var fenParts = [];
  var i;
  var x = 0;
  var fen = '';
  for (i = 0; i < squares.length; i++) {
    if (squares[i].piece != null) {
      if (x > 0) {
        fen = fen.concat(x);
        x = 0;
      }
      var notation = squares[i].piece.notation;
      if(notation == "") {
        notation = 'P';
      }
      if (squares[i].piece.side.name == 'black') {
        notation = notation.toLowerCase();
      }
      fen = fen.concat(notation);
    } else {
      x++;
    }

    if(squares[i].file == 'h') {
      if (x > 0) {
        fen = fen.concat(x);
        x = 0;
      }
      fenParts.push(fen);
      fen = '';
    }
  }
  fen = '';
  var i;
  for (i= fenParts.length-1; i>=0; i--) {
    fen = fen.concat(fenParts[i]);
    if(i> 0) {
      fen = fen.concat('/');
    }

  }
  var turn = (madeMoves.length %2 == 0) ? 'w' : 'b';
  fen = fen.concat(" ");
  fen = fen.concat(turn);
  fen = fen.concat(" ");
  fen = fen.concat(castlings);
  return fen;

},

determineCastlings: function(move) {
    if(move.prevSquare.file == 'h' && move.prevSquare.rank == 1) {
      castlings = castlings.replace('K', '');
    }

  if(move.prevSquare.file == 'a' && move.prevSquare.rank == 1) {
      castlings = castlings.replace('Q', '');
  }

  if(move.prevSquare.file == 'h' && move.prevSquare.rank == 8) {
      castlings = castlings.replace('k', '');

  }
  if(move.prevSquare.file == 'a' && move.prevSquare.rank == 8) {
      castlings = castlings.replace('q', '');

  }

  if(move.prevSquare.file == 'e' && move.prevSquare.rank == 1) {
    castlings = castlings.replace('K', '');
    castlings = castlings.replace('Q', '');

  }
  if(move.prevSquare.file == 'e' && move.prevSquare.rank == 8) {
    castlings = castlings.replace('k', '');
    castlings = castlings.replace('q', '');
  }
  if(castlings == '') {
    castlings = '-';

  }
},

checkEnPassant: function(move) {
  let rankDiff = abs(move.postSquare.rank-move.prevSquare.rank);
  if(if rankDiff == 2 and move.postSquare.piece.type == 'pawn') {


  }
},

getAdjacentRight: function(file, rank) {
  

}

};
