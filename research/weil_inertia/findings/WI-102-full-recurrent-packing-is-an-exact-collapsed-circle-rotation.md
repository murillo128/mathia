# WI-102 — Full recurrent packing is an exact collapsed-circle rotation

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + STRUCTURAL-CLASSIFICATION`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It sharpens the residual close-prime Ramanujan classification of WI-088/WI-096/WI-099/WI-100 at the equality boundary of the cycle-packing argument. When every available domain vertex is recurrent, the partial two-translation map is not an exotic interval-translation extremizer: its deleted source and sink intervals must coincide, and after collapsing that common interval the whole map is exactly one finite cyclic rotation. Consequently the fully packed cross-Gram rank defect has a closed gcd formula. Moreover, in any recurrent sector the first positive packing slack is at least two: one unused domain vertex is impossible.

Let `p<q<2p` be distinct odd primes, put

\[
d=q-p,
\qquad
t=p-d=2p-q,
\]

and work in the genuinely residual exceptional strip of WI-088/WI-096,

\[
\delta=kq+s,
\qquad
\delta>q-1,
\qquad
d<s<p.
\tag{1}
\]

Use

\[
A=\{0,\ldots,s-d-1\},
\qquad
C=\{s-d,\ldots,s-1\},
\qquad
B=\{s,\ldots,p-1\},
\tag{2}
\]

with `D=A\cup B`, and the forced-zero interval

\[
Z=kd+\{0,1,\ldots,d-1\}\pmod p.
\tag{3}
\]

WI-088 proves that

\[
g:D\longrightarrow (\mathbf Z/p\mathbf Z)\setminus Z
\tag{4}
\]

is a bijection, where

\[
g(j)=
\begin{cases}
j+(k+1)d,&j\in A,\\
j+kd,&j\in B
\end{cases}
\pmod p.
\tag{5}
\]

Its graph is a disjoint union of directed source-to-sink paths and free directed cycles. Let `F` be the union of all free cycles. WI-099 shows that whenever `F` is nonempty all free cycles have one common length `ell`; write their number as `c`. WI-096 gives the exact residual row-rank defect

\[
\tau_{p,q}(\delta)=\max\{0,c-1\}.
\tag{6}
\]

Following WI-100, define the exact packing slack

\[
\boxed{U:=t-|F|=t-c\ell}
\tag{7}
\]

when free cycles exist. The new equality classification is

\[
\boxed{
U=0
\iff
Z=C
\iff
s=[(k+1)d]_p,
}
\tag{8}
\]

where `[x]_p` denotes the least residue in `{0,\ldots,p-1}`. Under these equivalent conditions, put

\[
R:=s-d=[kd]_p,
\qquad 0<R<t.
\tag{9}
\]

Then the whole recurrent map is conjugate to the finite rotation

\[
\boxed{x\longmapsto x+R\pmod t.}
\tag{10}
\]

Hence

\[
\boxed{
c=\gcd(R,t),
\qquad
\ell=\frac{t}{\gcd(R,t)},
}
\tag{11}
\]

and therefore the fully packed cross-Gram defect and rank are exactly

\[
\boxed{
\tau_{p,q}(\delta)=\gcd(s-d,2p-q)-1,
}
\tag{12}
\]

\[
\boxed{
\operatorname{rank}G_{p,q}^{(N)}
=p-\gcd(s-d,2p-q).
}
\tag{13}
\]

Finally, if at least one free cycle exists, then

\[
\boxed{U\ne1.}
\tag{14}
\]

Thus in the recurrent sector the equality boundary is separated from every genuinely non-full packing by an integer gap:

\[
\boxed{U=0\quad\text{or}\quad U\ge2.}
\tag{15}
\]

## 1. Zero packing slack is exactly coincidence of the two deleted intervals

The domain has size

\[
|D|=p-d=t.
\tag{16}
\]

Every point of `F` lies in `D`. Therefore `U=0` is exactly `F=D`. In that case `g(D)=D`. But WI-088 gives the exact image identity

\[
g(D)=(\mathbf Z/p\mathbf Z)\setminus Z,
\tag{17}
\]

while by definition

\[
D=(\mathbf Z/p\mathbf Z)\setminus C.
\tag{18}
\]

Hence

\[
U=0\Longrightarrow Z=C.
\tag{19}
\]

Conversely, if `Z=C`, then (17)--(18) make `g:D\to D` a permutation of the finite set `D`. Every point of a finite permutation lies on a directed cycle, so `F=D` and `U=0`. Thus

\[
\boxed{U=0\iff Z=C.}
\tag{20}
\]

The interval `C=[s-d,s-1]` is an ordinary nonwrapping interval because `d<s<p`. Equality with the cyclic interval (3) therefore forces its initial point to be the least residue of `kd`:

\[
[kd]_p=s-d.
\tag{21}
\]

Adding `d` and using `s<p` gives

\[
[(k+1)d]_p=s.
\tag{22}
\]

Conversely, (22) with `s>d` gives (21), hence `Z=C`. This proves all equivalences in (8). In particular, full recurrence is not a diffuse equality case of WI-100's capacity inequality: it occurs on one exact boundary congruence.

## 2. Collapsing the common hole gives a literal rotation

Assume (8) and set `R=s-d`. Then

\[
C=Z=\{R,R+1,\ldots,R+d-1\},
\tag{23}
\]

with

\[
0<R<R+d=s<p.
\tag{24}
\]

The domain is

\[
D=\{0,\ldots,R-1\}\cup\{R+d,\ldots,p-1\}.
\tag{25}
\]

Collapse the common deleted interval by the order-preserving bijection

\[
\phi:D\longrightarrow\mathbf Z/t\mathbf Z,
\qquad
\phi(j)=
\begin{cases}
j,&0\le j<R,\\
j-d,&R+d\le j<p.
\end{cases}
\tag{26}
\]

where `t=p-d`. Equations (21)--(22) say that the two branch translations in (5) reduce modulo `p` to

\[
kd\equiv R,
\qquad
(k+1)d\equiv R+d.
\tag{27}
\]

For `j<R`, one has `g(j)=j+R+d (mod p)`. If this does not wrap modulo `p`, collapsing the deleted `d` sites subtracts `d`, giving `phi(g(j))=j+R`; if it wraps, the same identity is `phi(g(j))=j+R-t`. Thus in either case

\[
\phi(g(j))=\phi(j)+R\pmod t.
\tag{28}
\]

For `j>=R+d`, the branch displacement is `R` modulo `p`; the same nonwrapping/wrapping split gives again

\[
\phi(g(j))=\phi(j)+R\pmod t.
\tag{29}
\]

Therefore

\[
\boxed{
\phi\circ g\circ\phi^{-1}(x)=x+R\pmod t,
}
\tag{30}
\]

which proves the exact conjugacy (10).

A rotation by `R` on `Z/tZ` has exactly `gcd(R,t)` cycles, all of common length `t/gcd(R,t)`. Equations (11)--(13) now follow from the elementary finite rotation count together with WI-096's exact identity `tau=c-1` when cycles exist.

This also identifies the WI-099/WI-101 resonance data explicitly at equality. Writing

\[
g_0:=\gcd(R,t),
\qquad
\ell=t/g_0,
\tag{31}
\]

the rotation speed within one ordered cycle is

\[
\boxed{u=R/g_0,\qquad\gcd(u,\ell)=1.}
\tag{32}
\]

WI-101's identity `u congruent d m (mod ell)` therefore recovers the common arithmetic resonance from the collapsed-circle rotation. In particular the denominator of a fully packed defect is a genuine divisor of `t=2p-q`, not merely an abstract low-denominator witness.

## 3. The examples behind the one-third and one-fifth layers are the same rotation formula

The exact formula contains both the sharp three-cycle center and higher-denominator full packings.

For the WI-091 center

\[
(p,q,\delta)=(17,19,107),
\qquad
(k,s)=(5,12),
\tag{33}
\]

one has

\[
d=2,
\quad t=15,
\quad R=s-d=10,
\quad\gcd(R,t)=5.
\tag{34}
\]

Hence the domain is five cycles of length three and

\[
\tau=5-1=4,
\qquad
\operatorname{rank}G=12,
\tag{35}
\]

which is the sharp one-third center of WI-087/WI-091.

The non-three-cycle example already recorded in WI-096,

\[
(p,q,\delta)=(17,19,65),
\qquad
(k,s)=(3,8),
\tag{36}
\]

has

\[
R=6,
\qquad
\gcd(6,15)=3.
\tag{37}
\]

Thus it is three cycles of length five and

\[
\tau=2,
\tag{38}
\]

again without solving any row-kernel system. The apparent difference between the `ell=3` and `ell=5` full-packing examples is only the divisor structure of the same collapsed rotation.

As a useful corollary, if `t=2p-q` is prime, every fully packed residual map has `gcd(R,t)=1` because `0<R<t`; hence it has one free cycle and **zero** row-rank defect. More generally, a nonzero fully packed defect requires `t` to be composite, and its common cycle denominator is exactly the proper odd divisor `t/gcd(R,t)`.

## 4. One unit of positive slack is impossible

Assume now that at least one free cycle exists and suppose for contradiction that

\[
U=1.
\tag{39}
\]

The path/cycle decomposition of the WI-088 partial bijection has exactly `d` path components, one starting at each indegree-zero vertex of `Z` and one ending at each outdegree-zero vertex of `C`. A path with `L` directed edges contains exactly `L` vertices of `D`; its terminal vertex lies in `C` and is not counted in `D`. Hence

\[
U=\sum_{\text{path components}}L.
\tag{40}
\]

If `U=1`, precisely `d-1` paths have length zero and one path has length one. A zero-length path is exactly a vertex in `Z\cap C`, so

\[
|Z\cap C|=d-1.
\tag{41}
\]

Because a free cycle exists, WI-101's exact no-carry lemma applies: if

\[
R=[kd]_p,
\tag{42}
\]

then

\[
0<R<R+d<p.
\tag{43}
\]

Thus both `Z=[R,R+d-1]` and `C=[s-d,s-1]` are ordinary intervals of length `d`. Two distinct such intervals overlap in `d-1` points only when their starting points differ by `+1` or `-1`.

First let

\[
s-d=R+1.
\tag{44}
\]

Then the unique path source is `R` and the unique sink is `R+d`. Since `R` lies in `A`, its edge is

\[
g(R)\equiv R+(R+d)=2R+d\pmod p,
\tag{45}
\]

using the no-carry residue `[(k+1)d]_p=R+d`. For this one edge to end at `R+d` would require `R congruent 0 (mod p)`, contradicting (43).

The other possibility is

\[
s-d=R-1.
\tag{46}
\]

Then the unique source is `R+d-1` and the unique sink is `R-1`. The source lies in `B`, so

\[
g(R+d-1)\equiv (R+d-1)+R\pmod p.
\tag{47}
\]

For this to equal `R-1` would require

\[
R+d\equiv0\pmod p,
\tag{48}
\]

again impossible by (43). Therefore `U=1` cannot occur whenever recurrence is present, proving (14)--(15). The bound is sharp at the next integer: exact small-prime enumeration contains recurrent examples with `U=2`, so no universal strengthening to `U>=3` is available from this argument.

## 5. Stress tests and prior-art boundary

The theorem is exact and depends only on WI-088's source/sink partial bijection, WI-096's exact free-cycle rank formula, and for the `U=1` exclusion WI-101's no-carry lemma. The full-packing equivalence and rotation conjugacy do not use numerical rank tolerance, prime-distribution asymptotics, random-matrix heuristics, or an unproved Yang input.

As falsification only, an exact finite enumeration of all admissible residual parameters for close prime pairs with smaller prime below `150` found no counterexample to (8), (11), or (12): every zero-slack instance obeyed `s=[(k+1)d]_p`, and its measured cycle count was exactly `gcd(s-d,t)`. The previously completed smaller sweep of the nonzero-defect recurrent sector found no `U=1` instance. These computations are not used as evidence for the theorem.

The literature audit separates three standard backgrounds from the arithmetic specialization here. The path/cycle decomposition is standard finite partial-permutation theory. Poincare rotation theory and the double-rotation/interval-translation literature describe the surrounding dynamical mechanism; relevant sources include Suzuki--Ito--Aihara, **Double rotations**, *Discrete and Continuous Dynamical Systems* 13 (2005), 515--532, DOI `10.3934/dcds.2005.13.515`, and Bruin--Clack, **Inducing and unique ergodicity of double rotations**, *DCDS* 32 (2012), 4133--4147. The recent Drach--Staresinic--van Strien preprint **Transversality for Interval Translation Maps**, arXiv:2605.00173 (2026), studies a much broader continuous ITM setting. Vaidyanathan's **Ramanujan Sums in the Context of Signal Processing—Part I**, *IEEE Transactions on Signal Processing* 62 (2014), 4145--4157, DOI `10.1109/TSP.2014.2331617`, supplies the standard Ramanujan-subspace framework.

Those sources do not supply the finite-window prime cross-Gram partial map, the exact deleted-interval equality (8), or the rank formula (12)--(13). The closest internal antecedents are WI-099's common-rotation theorem and WI-100's capacity slack `U`; neither identifies the zero-slack map itself as a collapsed rotation or gives the gcd rank formula. No priority claim is made for this specialization.

## 6. Program consequence

WI-100 left the near-saturated residual sector parametrized by a common cycle type plus a packing slack. The equality endpoint is now completely rigid. There is no hidden family of fully packed two-translation extremizers to classify: after the source and sink holes coincide, the problem collapses exactly to a rotation of `Z/(2p-q)Z`, and the rank defect is only the elementary gcd in (12).

This is a stopping rule for one natural pairwise route. Searching the `U=0` sector for additional cyclotomic, Loewner, or interval-translation structure cannot produce a different rank scale: every such representation must reproduce the same rotation cycles. Any genuinely new pairwise structure must enter at positive slack, where (15) shows that the first departure already consumes at least two domain vertices, or must use information absent from the scalar pair map—simultaneous/source-labelled consistency, many-modulus welding, metric coherence, or the full locked Yang covariance.

The result also sharpens equality/near-equality auditing under the canonical research mandate. Exact saturation is characterized by one congruence and one gcd, so future many-pair arguments can separate this algebraically rigid sector before estimating the positive-slack residual family.