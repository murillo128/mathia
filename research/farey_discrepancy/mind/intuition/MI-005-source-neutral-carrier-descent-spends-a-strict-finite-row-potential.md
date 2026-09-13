# MI-005 — Adaptive nonhead descent has a sharp carrier-free logarithmic source budget

**Evidence level:** proved for the current nonhead predecessor branches by [FD-102](../../findings/FD-102-adaptive-nonhead-retagging-has-an-exact-logarithmic-source-budget.md); [FD-103](../../findings/FD-103-power-dense-record-ladders-saturate-the-logarithmic-source-budget.md) shows the logarithmic coefficient is geometrically sharp on actual source-record carriers. No logarithmic-depth packet-transport theorem or RH contradiction is claimed.

FD-100--FD-101 first show that a fixed/tagged nonhead carrier cannot preserve one source quotient indefinitely: row inventory drains, and floor/ceiling drift changes the source shell at most once before exactifying the carrier. FD-102 removes the remaining retagging loophole entirely at the geometric level.

For a nonhead state at horizon `H` sampling source quotient `x`, define

`A(H,x)=log_2((H-1)/(8x-1))`.

Every current nonhead predecessor satisfies `H'<=ceil(H/2)`. After arrival the packet may retag onto **any** nonhead row with new source quotient `y`, yet

`A(H',y) <= A(H,x)-1 + log_2((8x-1)/(8y-1))`.

Hence carrier switching cannot reset source-neutral inventory for free. If the retag does not move to a smaller source (`y>=x`), one full unit of `A` is spent. Along any `m` consecutive nonhead predecessor states, irrespective of carrier identity,

`8x_m-1 <= (H_0-1)/2^m`.

A segment that never drops below its initial source scale therefore has length at most `A(H_0,x_0)`. On the false-RH frontier core this is

`m <= (1-Theta+delta+o(1)) log_2 H_0`.

FD-103 shows that this is not merely a proof artifact. Power-dense strict source records seed dyadic nonhead ladders with constant sampled source `X`, and those ladders satisfy

`m=A(2^k X,X)+o(1)`.

At frontier scaling `X=H_0^(Theta+o(1))` they realize the coefficient `(1-Theta+o(1)) log_2 H_0`. Their intrinsic projective quality remains only polynomially small, with the top-scale lower bound `H_0^(-2Theta(1-Theta)-o(1))`. Thus no argument using only horizon contraction, row eligibility, floor geometry or source-record recurrence can shorten the logarithmic source-neutral window.

The live obstruction has moved from **retagging** to **packet strength across logarithmic depth**. The deterministic geometry already forces either a head, genuine source descent, or exhaustion after `c log H` nonhead steps. What is missing is a uniform predecessor-energy theorem showing that sufficiently strong mass survives long enough for this deterministic budget to matter, or an argument that extracts enough progress from the intervening head/source-descending events.

**Boundary.** FD-103 supplies matched sharp carriers, not a counterexample to a future fixed-occupation packet theorem. The projective quality bound is polynomial and does not by itself guarantee the packet strength required at every step.