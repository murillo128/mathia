# Weil Inertia residual-defect triangular islands

![Exact residual defect and WI-100 capacity bound across the boundary remainder](weil-inertia-defect-triangles.png)

## Question

WI-096 makes the residual prime Ramanujan row-rank defect exactly computable as a free-cycle count, while WI-099 makes each nonzero state phase-pure and WI-100 gives a resonance-dependent capacity tent. The visual question was whether the *actual* defect inside those capacity regions has a simpler geometric profile than the existing upper bound suggests.

## Construction

For odd coprime moduli `p<q<2p`, put `d=q-p` and use the WI-096 residual partial map at

\[
\delta=kq+s,\qquad d<s<p.
\]

With

\[
A=\{0,\ldots,s-d-1\},\quad
C=\{s-d,\ldots,s-1\},\quad
B=\{s,\ldots,p-1\},
\]

the map on `D=A union B` is

\[
g(j)=
\begin{cases}
j+(k+1)d \pmod p,&j\in A,\\
j+kd \pmod p,&j\in B.
\end{cases}
\]

The forced-zero interval is `Z=kd+{0,...,d-1} mod p`. I counted the directed free cycles of `g` exactly and plotted

\[
\tau(s)=\max\{0,c(s)-1\},
\]

which equals the prime-pair row-rank defect by WI-096. For each positive state, the dashed curve is the WI-100 capacity upper bound

\[
\min\left\{
\left\lfloor\frac{s-d}{a}\right\rfloor,
\left\lfloor\frac{p-s}{\ell-a}\right\rfloor
\right\}-1,
\]

using the common phase `(m,\ell)` and `a=mp-\ell k` supplied by WI-099.

The rendered example fixes `p=149`, `q=151`, and `k=45` and scans every admissible `s`. Labels above the peaks give the reduced resonance `m/\ell`.

## Observation

The positive defect does not fill the capacity envelope. It breaks into separated resonance islands, and every island in the example is an exact integer triangle with unit slopes. The five visible components are:

- `m/ell=13/43`, `s=9..11`, with defect `1,2,1`;
- `10/33`, `s=24..26`, with defect `1,2,1`;
- `7/23`, `s=51..57`, with defect `1,2,3,4,3,2,1`;
- `15/49`, `s=91..93`, with defect `1,2,1`;
- `4/13`, `s=118..136`, with defect rising from `1` to `10` and then back to `1`.

Thus the picture suggests a stronger local law than the capacity upper tent: if `[L,R]` is one connected positive-defect component, then

\[
\tau(s)\stackrel{?}{=}\min\{s-L+1,\;R-s+1\}.
\]

## Robustness

I exhaustively evaluated the exact WI-096 partial-map combinatorics for every distinct odd prime pair with `11 <= p < 150`, `p<q<2p`, every `1 <= k <= floor((p-1)/2)`, and every admissible residual/nearest-boundary remainder `s`. Across `2,783` connected positive-defect components and `22,193` positive parameter points, there was no violation of the displayed triangular formula.

As a matched structural control, I repeated the same partial-map experiment with odd composite `p` in `11 <= p < 100` and every odd coprime `q` with `p<q<2p`. Across `3,404` positive components and `21,768` positive points, every component was a unit-slope tent segment. All `2,868` components lying strictly inside the admissible `s` range were exact symmetric triangles by the same formula; the remaining components were truncated by the scan boundary.

This control is important: the triangular geometry appears to survive after primality is removed. The current evidence therefore points toward a universal cyclic-order/partial-rotation phenomenon rather than a prime-specific arithmetic signal. These are exact finite computations, not a general proof.

## Research consequence

This visualization motivates the proposed Weil Inertia clue [Is every residual Ramanujan defect sector an exact triangular island?](../../weil_inertia/clues/CLUE-residual-defect-triangular-islands.md).

The image and finite enumerations are exploratory support only. They do not establish the general triangular law, its endpoint formula, novelty, or any consequence for the Yang--Yang fourth-moment program or RH.
