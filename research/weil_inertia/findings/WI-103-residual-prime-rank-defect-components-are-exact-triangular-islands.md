# WI-103 — Residual prime Ramanujan rank-defect components are exact triangular islands

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-CLASSIFICATION + DECISIVE-NEGATIVE`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It resolves the prime part of `CLUE-weil-inertia-residual-defect-triangular-islands`: in the WI-088/WI-096 genuinely residual close-prime regime, every connected positive-defect component as the boundary remainder moves is an exact symmetric integer triangle with unit slopes. More strongly, once one recurrent rotation phase `(m,ell)` occurs, all of its free cycles are integer translates of one uniquely determined cyclic gap template, and the phase support is the overlap convolution of two intervals of the **same** length. The equality of those two lengths is forced by the two branch transitions of the partial rotation; it is not a numerical coincidence.

Let `p<q<2p` be distinct odd primes, put

\[
d=q-p,
\qquad
t=p-d=2p-q,
\]

and fix the quotient `k` in the genuinely residual strip

\[
\delta=kq+s,
\qquad
d<s<p.
\tag{1}
\]

It is convenient to write

\[
S:=s-d,
\]

so that

\[
A=\{0,\ldots,S-1\},
\quad
C=\{S,\ldots,S+d-1\},
\quad
B=\{S+d,\ldots,p-1\}.
\tag{2}
\]

The WI-088 partial bijection is

\[
g(j)=
\begin{cases}
j+(k+1)d,&j\in A,\\
j+kd,&j\in B,
\end{cases}
\pmod p.
\tag{3}
\]

WI-096 proves that, if `c(S)` is its free-cycle count, the exact residual row-rank defect is

\[
\boxed{\tau(S)=\max\{0,c(S)-1\}.}
\tag{4}
\]

WI-099 proves phase purity: whenever free cycles exist, all of them have one common length `ell`, one common number `a` of visits to `A`, and one reduced resonance `m/ell`, with

\[
\ell k+a=mp,
\qquad
1\le a<\ell,
\qquad
\gcd(m,\ell)=1.
\tag{5}
\]

WI-101 proves the no-carry property and the common cyclic rotation step. Put

\[
h=\left\lfloor\frac{kd}{p}\right\rfloor,
\qquad
R=kd-hp.
\tag{6}
\]

Then recurrence forces

\[
0<R<R+d<p,
\tag{7}
\]

and, after the `ell` points of any free cycle are listed in ambient cyclic order, `g` advances by

\[
\boxed{u=dm-\ell h,\qquad 1\le u<\ell,\qquad\gcd(u,\ell)=1.}
\tag{8}
\]

The new theorem is that each such phase has one explicit triangular support, and distinct phase supports cannot overlap.

## 1. Every cycle of one phase has the same cyclic gap word

Take one free cycle of the common phase and list its points as

\[
0\le y_0<y_1<\cdots<y_{\ell-1}<p.
\tag{9}
\]

Let its positive cyclic gaps be

\[
b_i=y_{i+1}-y_i\quad(0\le i<\ell-1),
\qquad
b_{\ell-1}=p+y_0-y_{\ell-1}.
\tag{10}
\]

Because `A` is the initial interval and `B` is the final interval, while a free cycle avoids the deleted interval `C`, the first `a` ordered points are exactly the `A` points. Thus, with indices modulo `ell`,

\[
\varepsilon_i=
\begin{cases}1,&0\le i<a,\\0,&a\le i<\ell,
\end{cases}
\tag{11}
\]

records the branch of the source `y_i`.

By (7), the positive clockwise displacement of an `A` edge is `R+d`, while that of a `B` edge is `R`. Since `g(y_i)=y_{i+u}`, one has the exact arc equations

\[
\boxed{
\sum_{r=0}^{u-1}b_{i+r}=R+d\varepsilon_i
\qquad(i\bmod\ell).
}
\tag{12}
\]

Subtracting the equation at `i` from the one at `i+1` gives

\[
\boxed{
b_{i+u}-b_i=d(\varepsilon_{i+1}-\varepsilon_i).}
\tag{13}
\]

There are only two nonzero right-hand sides: `-d` at `i=a-1` and `+d` at `i=ell-1`. Since addition by `u` is a single cycle on `Z/ell Z`, equation (13) forces the entire gap vector to take exactly two values

\[
\boxed{b_i\in\{b,b+d\}.}
\tag{14}
\]

Moreover the wrap gap is low and the `A/B` transition gap is high:

\[
\boxed{b_{\ell-1}=b,\qquad b_{a-1}=b+d.}
\tag{15}
\]

Indeed (13) at `ell-1` raises the value by `d`, and following the `+u` orbit keeps that high value until the unique downward jump after `a-1`; after that the value stays low until returning to `ell-1`.

Let `H` be the number of high gaps. Equivalently, `H` is the unique integer `1<=H<ell` satisfying

\[
Hu\equiv a\pmod\ell.
\tag{16}
\]

The high indices are explicitly

\[
\boxed{
\mathcal H
=\{[ru-1]_{\ell}:1\le r\le H\},
}
\tag{17}
\]

where `[.]_ell` is the least residue modulo `ell`. Since `u congruent dm (mod ell)` and `a congruent mp (mod ell)`, (16) is equivalent to

\[
Hd\equiv p\pmod\ell.
\tag{18}
\]

WI-101 gives `gcd(d,ell)=1`, so `H` is also the least positive residue

\[
\boxed{H=[p d^{-1}]_{\ell}.}
\tag{19}
\]

Summing the cyclic gaps yields

\[
p=\ell b+Hd,
\]

hence

\[
\boxed{b=\frac{p-Hd}{\ell}>0.}
\tag{20}
\]

Equations (17)--(20) determine the whole gap word from `(p,d,m,ell)`:

\[
\boxed{
b_i=b+d\,1_{\{i\in\mathcal H\}}.}
\tag{21}
\]

Thus two free cycles of the same phase cannot have different shapes. They are translates of one canonical cyclic template.

For completeness, (12) is not lost when one reconstructs the gaps from (13). The two sides of (12) have the same successive differences by construction, hence differ by one constant. Summing over `i`, the left side is `up`; the right side is `ell R+ad`. But multiplying `ell k+a=mp` by `d` and using `kd=hp+R` gives

\[
up=(dm-\ell h)p=\ell R+ad.
\tag{22}
\]

Therefore that constant is zero and the reconstructed template satisfies the original branch displacements exactly.

## 2. The available cycle translates form one interval of length `b`

Define canonical offsets

\[
P_0=0,
\qquad
P_j=\sum_{i=0}^{j-1}b_i
\quad(1\le j<\ell).
\tag{23}
\]

Every free cycle of this phase has the form

\[
\boxed{
\mathcal O_x=\{x+P_0,\ldots,x+P_{\ell-1}\}
}
\tag{24}
\]

for its smallest point `x=y_0`. Since

\[
P_{\ell-1}=p-b
\tag{25}
\]

by (15) and the total gap sum, all points of (24) lie in `{0,...,p-1}` exactly when

\[
\boxed{0\le x\le b-1.}
\tag{26}
\]

So there are exactly `b` possible integer translates of the cyclic template before the `A/B` cut is imposed.

Let

\[
P:=P_{a-1}.
\tag{27}
\]

For `O_x` to be a free cycle at boundary position `S`, its first `a` points must lie in `A` and the remaining points in `B`. By monotonicity of the ordered template this is equivalent to the two endpoint inequalities

\[
x+P<S,
\qquad
x+P_a\ge S+d.
\tag{28}
\]

The decisive identity (15) gives

\[
P_a=P+b+d.
\tag{29}
\]

Hence (28) is exactly

\[
\boxed{
P+x+1\le S\le P+b+x.
}
\tag{30}
\]

For each translate `x`, the allowed `S` interval therefore has exactly `b` integer values. The number of possible translates is also exactly `b`. This equality is the source of the symmetric triangle.

Conversely, if (26) and (30) hold, the template points lie in `A union B`, equation (12) makes (3) send `y_i` exactly to `y_{i+u}`, and therefore `O_x` is a genuine free cycle. Thus there is no gap between the template count and the actual partial-map recurrence.

## 3. Exact cycle-count and defect triangles

From (26)--(30), the number of free cycles of this phase at `S` is exactly

\[
\boxed{
 c_{m/\ell}(S)
 =\#\Bigl(
 [0,b-1]\cap[S-(P+b),\,S-(P+1)]
 \Bigr).
}
\tag{31}
\]

This is the discrete convolution of two interval indicators of equal length `b`. Therefore its support is

\[
\boxed{
P+1\le S\le P+2b-1,
}
\tag{32}
\]

and on that support

\[
\boxed{
 c_{m/\ell}(S)
 =\min\{S-P,\,P+2b-S\}.
}
\tag{33}
\]

In particular the cycle count is

\[
1,2,\ldots,b-1,b,b-1,\ldots,2,1.
\tag{34}
\]

The whole support lies automatically in the residual range. The lower endpoint in (32) is positive. For the upper endpoint, `a<ell` gives

\[
P_a\le P_{\ell-1}=p-b.
\]

Using `P_a=P+b+d`,

\[
P+2b\le p-d=t,
\tag{35}
\]

so `P+2b-1<=t-1` as required.

Returning to the original remainder `s=S+d`, the one-cycle support is

\[
\boxed{
 d+P+1\le s\le d+P+2b-1.
}
\tag{36}
\]

If `b=1`, this phase contributes exactly one free cycle at one boundary and therefore zero row-rank defect by WI-096. If `b>=2`, its positive-defect interval is

\[
\boxed{
L=d+P+2,
\qquad
R=d+P+2b-2,
}
\tag{37}
\]

and equations (4) and (33) give the exact formula

\[
\boxed{
\tau(s)=\min\{s-L+1,\;R-s+1\}
\qquad(L\le s\le R).
}
\tag{38}
\]

The apex is at

\[
\boxed{s_*=d+P+b,\qquad \tau(s_*)=b-1.}
\tag{39}
\]

This proves the triangular-island formula conjectured by the clue.

## 4. Different resonance phases cannot splice into one positive component

For fixed `(p,q,k)`, several reduced fractions `m/ell` may satisfy the quotient relation `k=floor(mp/ell)`. This is exactly what appears in the visual experiment behind the clue. The preceding proof gives one support interval for every phase that actually occurs.

Those one-cycle support intervals are pairwise disjoint. If supports of two distinct phases overlapped at some `S`, equation (31) would construct at least one genuine free cycle of each phase at that same `S`. This contradicts WI-099, which proves that **all** free cycles at one residual boundary have one common reduced phase.

Consequently the positive interiors of two phase supports are separated by at least one zero-defect boundary value. A maximal connected interval on which `tau>0` therefore belongs to one and only one phase, and (38) is the defect profile of the whole connected component rather than merely of a selected resonance subfamily.

This also supplies an explicit endpoint algorithm from the WI-099/WI-101 phase. Given `(p,d,k,m,ell)`, compute

\[
a=mp-\ell k,
\qquad
u=dm-\ell\left\lfloor\frac{kd}{p}\right\rfloor,
\tag{40}
\]

then `H` from (16) or (19), `b` from (20), the high-gap set from (17), and

\[
P=(a-1)b+d\,\#\{1\le r\le H:[ru-1]_{\ell}<a-1\}.
\tag{41}
\]

Equations (37) then give `L,R` without enumerating the partial-map graph or solving a Fourier rank problem.

## 5. The visual `p=149,q=151,k=45` example becomes exact arithmetic

For the largest displayed island in the exploratory visualization,

\[
(p,q,k)=(149,151,45),
\qquad
(m,\ell)=\left(4,13\right).
\tag{42}
\]

Here

\[
d=2,
\quad
a=11,
\quad u=8,
\quad H=3,
\quad b=11.
\tag{43}
\]

The high-gap indices from (17) are `2,7,10`, so the canonical gaps are eleven except for three gaps of size thirteen. Equation (41) gives

\[
P=P_{10}=114.
\tag{44}
\]

Therefore

\[
L=2+114+2=118,
\qquad
R=2+114+22-2=136,
\tag{45}
\]

and

\[
\tau(s)=1,2,\ldots,10,\ldots,2,1
\qquad(118\le s\le136),
\tag{46}
\]

with apex at `s=127`. These are exactly the values observed in the read-only visual experiment, now as a consequence of (12)--(38) rather than finite scanning.

The same formulas recover its other four positive components (`13/43`, `10/33`, `7/23`, `15/49`) and explain why many additional arithmetic candidate denominators produce no positive defect: phases with `b=1` can support at most one free cycle, which WI-096 removes through the global zero-mean relation.

As falsification only, the proof was independently replayed against the exact partial map on additional prime configurations beyond the original `p<150` visualization range. Forty fixed `(p,q,k)` configurations with `151<=p<360`, chosen to include low-denominator resonance quotients and random quotients, contained 36 positive components; every measured component had the endpoints from (37) and the pointwise defect from (38). This finite check is not used as evidence for the theorem.

## 6. Prior-art boundary and the composite control

The surrounding dynamical system is a finite two-translation / interval-translation map. Suzuki, Ito and Aihara, **Double rotations**, *Discrete and Continuous Dynamical Systems* 13 (2005), 515--532, DOI `10.3934/dcds.2005.13.515`, study the continuous double-rotation family and its reduction to rotations. Bruin and Clack, **Inducing and unique ergodicity of double rotations**, *DCDS* 32 (2012), 4133--4147, develop the corresponding induction theory. Classical rational-rotation gap codings are also adjacent to mechanical/Christoffel words; see Christophe Reutenauer, *From Christoffel Words to Markoff Numbers*, Oxford University Press (2019), especially the cyclic/conjugacy viewpoint on Christoffel words.

Those sources explain why two-valued cyclic gap words and rotation codings are natural nearby objects, but the located statements do not give the WI-088 finite deleted-source/deleted-sink map, the exact recurrence (13), or the equal-length interval convolution (31) that produces the Ramanujan defect triangle. No priority claim is made for this specialization.

The proof above is stated only at the evidence level already established for the **prime residual** phase theorems WI-096/WI-099/WI-101. Much of the argument visibly needs only coprimality and the no-carry/phase-purity conclusions, which explains why the read-only visual control found the same triangular geometry for many odd coprime composite moduli. However, this finding does not silently promote those prime antecedents to a fully audited composite theorem. The safe structural statement is conditional: any odd-coprime partial-rotation instance satisfying the same common `(a,ell,u)` phase and no-carry hypotheses obeys (12)--(38). A complete unconditional composite classification remains a separate task if it becomes relevant.

## 7. Program consequence

The triangular islands are now a **universal consequence of the one-pair cyclic-order model**, not evidence of extra prime arithmetic. Their shape comes from three exact facts: phase purity fixes one ordered rotation; the two branch transitions force the orbit gap word to have low/high gaps differing by exactly `d`; and the low wrap gap equals the high `A/B` transition gap minus `d`. That last identity makes the number of possible orbit translates equal to the number of boundary positions supporting each translate, and interval overlap then forces the unit-slope symmetric triangle.

Accordingly, trying to exploit the visible triangular profile itself as a new source of Yang cancellation would double-count information already present in the pairwise partial-map geometry. What remains potentially useful is the closed endpoint/height parametrization: a nonzero phase has exact peak defect

\[
\boxed{\tau_{\max}=b-1
=\frac{p-Hd}{\ell}-1,
\qquad
H=[p d^{-1}]_{\ell},}
\tag{47}
\]

and exact support (36)--(41). This replaces pointwise free-cycle enumeration by arithmetic resonance intervals and may simplify future many-modulus incidence or source-labelled welding arguments. Any further improvement of the fourth-moment program must use simultaneous coupling between different pair interactions, actual Yang coefficients, cross-scale structure, or another invariant not determined by these universal one-pair triangles.