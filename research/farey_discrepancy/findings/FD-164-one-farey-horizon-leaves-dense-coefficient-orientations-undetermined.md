# FD-164 — One Farey horizon leaves dense coefficient orientations undetermined

- **Date:** 2026-09-16
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact matched-control obstruction / same-horizon information boundary / source-bridge test
- **Depends on:** FD-009, FD-117, FD-118, FD-163
- **Classification:** `EXACT-DERIVED + MATCHED-SQUAREFREE-UNIT-CONTROL + NEGATIVE/INFORMATION-BRIDGE`

## Claim

`FD-117` and `FD-118` show that the complete Farey discrepancy field at one horizon `T` is exactly equivalent to the floor-quotient Mertens staircase

\[
\mathcal Q_T:=\left\{\left\lfloor\frac Tm\right\rfloor:1\le m\le T\right\},
\qquad
\bigl(M(r)\bigr)_{r\in\mathcal Q_T}.
\tag{1}
\]

The same-horizon compression is much more severe than a formal dimension count suggests. Even after imposing the exact Möbius support and amplitude law — zero on nonsquarefree integers and unit signs on squarefree integers — one can change asymptotically almost every coefficient in any positive-density squarefree subset while keeping **every coordinate in (1) exactly unchanged**.

Let

\[
V_T:=\{n\le T:\mu^2(n)=1\},
\qquad
Q_{\rm sf}(x):=|V_x|,
\tag{2}
\]

and fix an integer `K>=1`. Put

\[
q_j:=\left\lfloor\frac Tj\right\rfloor
\qquad(1\le j\le K+1).
\tag{3}
\]

For all sufficiently large `T` there exists a coefficient source

\[
a_T:\{1,\ldots,T\}\to\{-1,0,+1\}
\tag{4}
\]

such that

\[
a_T(1)=1,
\qquad
a_T(n)=0\iff\mu(n)=0,
\qquad |a_T(n)|=1\quad(n\in V_T),
\tag{5}
\]

and, writing

\[
A_T(x):=\sum_{n\le x}a_T(n),
\tag{6}
\]

one has the exact staircase match

\[
\boxed{
A_T(r)=M(r)
\qquad\text{for every }r\in\mathcal Q_T.
}
\tag{7}
\]

Nevertheless the number of changed squarefree coefficients is exactly

\[
\boxed{
\#\{n\in V_T:a_T(n)\ne\mu(n)\}
=
Q_{\rm sf}(T)-Q_{\rm sf}(q_{K+1})
-
\sum_{j=1}^{K}
\left|M(q_j)-M(q_{j+1})\right|.
}
\tag{8}
\]

The prime number theorem in the equivalent form `M(x)=o(x)`, together with the elementary squarefree count, therefore gives

\[
\boxed{
\frac{1}{|V_T|}
\#\{n\in V_T:a_T(n)\ne\mu(n)\}
=
\frac{K}{K+1}+o_K(1).
}
\tag{9}
\]

This also localizes to **every positive-density coefficient family**, not only to the whole squarefree set. If `D_T subseteq V_T` satisfies

\[
\liminf_{T\to\infty}\frac{|D_T|}{|V_T|}\ge\delta>0,
\tag{10}
\]

then the same construction obeys

\[
\boxed{
\frac{\#\{n\in D_T:a_T(n)\ne\mu(n)\}}{|D_T|}
\ge
1-
\frac{1}{\delta(K+1)}
-o_{K,\delta}(1).
}
\tag{11}
\]

Consequently, for every fixed `epsilon>0`, choosing `K` once with

\[
K+1>\frac{2}{\delta\epsilon}
\tag{12}
\]

makes a squarefree-unit matched source disagree with Möbius on at least a `1-epsilon` fraction of `D_T` for all sufficiently large `T`, while (7) remains exact.

The connection to the current ancestry architecture is immediate. Under the bounded-resource hypotheses of `FD-163`, its prime-avoidance anchor face `D_(S,T)` has a uniform positive lower density. Hence the **complete same-horizon Farey discrepancy field does not determine, even approximately in Hamming density, the Möbius orientations on the positive-density anchor face that the coercive architecture assumes**. A source-faithful proof must therefore add information that couples horizons or otherwise uses the actual Möbius law beyond the one-horizon quotient-Mertens staircase.

This is the missing information-boundary step after `FD-163`: positive geometric exposure is not yet source justification.

## 1. Balanced sign flips inside the macroscopic quotient shells

For `1<=j<=K`, let

\[
I_j:=(q_{j+1},q_j]\cap\mathbb Z
\tag{13}
\]

and split its squarefree integers according to their Möbius sign,

\[
P_j:=\{n\in I_j:\mu(n)=+1\},
\qquad
N_j:=\{n\in I_j:\mu(n)=-1\}.
\tag{14}
\]

Put

\[
m_j:=\min(|P_j|,|N_j|).
\tag{15}
\]

Choose arbitrary subsets `P'_j subseteq P_j` and `N'_j subseteq N_j` with

\[
|P'_j|=|N'_j|=m_j.
\tag{16}
\]

Define `a_T` by flipping the Möbius sign on these paired subsets and nowhere else:

\[
a_T(n):=
\begin{cases}
-\mu(n),&n\in\bigcup_{j=1}^{K}(P'_j\cup N'_j),\\
\mu(n),&\text{otherwise}.
\end{cases}
\tag{17}
\]

The construction never changes the zero set, never changes a nonzero amplitude, and never touches `1` once `T` is large. Inside one block the cumulative coefficient change has total

\[
\sum_{n\in I_j}(a_T(n)-\mu(n))
=-2|P'_j|+2|N'_j|=0.
\tag{18}
\]

Thus every modified macroscopic quotient shell has exactly zero net source change.

This is stronger than merely perturbing a real formal source in a nullspace: the control remains in the exact ternary squarefree-unit class used throughout the line.

## 2. Zero block sums preserve the complete floor-quotient staircase

For fixed `K` and sufficiently large `T`, one has `K+1<=sqrt(T)`, the values in (3) are distinct, and the floor-quotient set has the standard decomposition

\[
\mathcal Q_T
=
\{1,\ldots,\lfloor\sqrt T\rfloor\}
\cup
\left\{
\left\lfloor\frac Tj\right\rfloor:
1\le j\le\lfloor\sqrt T\rfloor
\right\}.
\tag{19}
\]

Every floor quotient larger than `q_(K+1)` is therefore one of

\[
q_1,\ldots,q_K.
\tag{20}
\]

Below `q_(K+1)` the source is unchanged. At `q_j`, the only changed integers that have entered the cumulative sum lie in complete blocks `I_j,I_(j+1),...,I_K`, each of which has zero total change by (18). Hence

\[
A_T(q_j)-M(q_j)=0
\qquad(1\le j\le K),
\tag{21}
\]

while the same equality is immediate for every floor quotient at or below `q_(K+1)`. This proves (7).

To make the implication for Farey discrepancy explicit, define for an arbitrary cumulative source `A` the formal field in the exact `FD-117` coordinates

\[
\mathcal D_{T,A}(x)
:=
x-\lfloor x\rfloor
+
\sum_{m\le T}
\bigl(\lfloor mx\rfloor-mx\bigr)
A\!\left(\left\lfloor\frac Tm\right\rfloor\right).
\tag{22}
\]

Every argument `floor(T/m)` in (22) lies in `Q_T`. Equation (7) therefore gives the pointwise identity

\[
\boxed{
\mathcal D_{T,A_T}(x)=D_T(x)
\qquad(0\le x\le1),
}
\tag{23}
\]

where `D_T` is the actual Farey discrepancy field. Equivalently, all Fourier coordinates of `FD-117`/`FD-118` agree as well. The matched source is invisible not merely to one scalar Franel statistic or a finite frequency packet but to the **entire same-horizon discrepancy function**.

## 3. Almost every squarefree sign in the modified macroscopic region can be changed

The number of changed coefficients in block `I_j` is

\[
2m_j
=
|P_j|+|N_j|-\bigl||P_j|-|N_j|\bigr|.
\tag{24}
\]

The first two terms count the squarefree integers in the block, while

\[
|P_j|-|N_j|
=
\sum_{n\in I_j}\mu(n)
=
M(q_j)-M(q_{j+1}).
\tag{25}
\]

Hence

\[
2m_j
=
Q_{\rm sf}(q_j)-Q_{\rm sf}(q_{j+1})
-
|M(q_j)-M(q_{j+1})|.
\tag{26}
\]

Summing (26) over `j=1,...,K` telescopes the squarefree term and proves the exact count (8).

For each fixed `j`, `q_j=T/j+O(1)`. The prime number theorem gives

\[
M(q_j)=o(T),
\tag{27}
\]

and the elementary identity `mu^2(n)=sum_(d^2|n)mu(d)` gives

\[
Q_{\rm sf}(x)
=
\frac{x}{\zeta(2)}+O(\sqrt x).
\tag{28}
\]

Because `K` is fixed before `T` tends to infinity,

\[
\sum_{j=1}^{K}|M(q_j)-M(q_{j+1})|=o_K(T).
\tag{29}
\]

Substituting (28)--(29) into (8), and using `q_(K+1)/T -> 1/(K+1)`, proves (9).

The role of the prime number theorem is deliberately isolated. The exact invisibility statement (7) and the exact mismatch count (8) are finite combinatorics. PNT is used only to show that, in each fixed-proportion quotient shell, the two Möbius signs are sufficiently balanced that almost every squarefree coefficient can participate in a zero-sum flip.

## 4. Positive-density anchor faces remain almost completely ambiguous

Let

\[
B_T:=\{n\in V_T:a_T(n)\ne\mu(n)\}.
\tag{30}
\]

By construction, every squarefree integer above `q_(K+1)` lies in `B_T` except for exactly

\[
U_T:=
\sum_{j=1}^{K}|M(q_j)-M(q_{j+1})|
=o_K(T)
\tag{31}
\]

unflipped squarefree positions. Therefore for any `D_T subseteq V_T`,

\[
|D_T\setminus B_T|
\le
Q_{\rm sf}(q_{K+1})+U_T.
\tag{32}
\]

Under (10), divide by `|D_T|` and use (28):

\[
\frac{|D_T\setminus B_T|}{|D_T|}
\le
\frac{1}{\delta(K+1)}+o_{K,\delta}(1),
\tag{33}
\]

which is (11).

Now impose the hypotheses of `FD-163`: there is a persistent nontrivial active auxiliary core and constants `h_0>0`, `P_0`, `L_0` such that

\[
h_{S,T}\ge h_0,
\qquad
P_{S,T}\le P_0,
\qquad
\frac{L_{S,D(c),T}}{2^{\omega(c)}}\le L_0.
\tag{34}
\]

That finding gives, with

\[
B:=\left\lceil\frac{2(P_0+L_0)}{h_0}\right\rceil,
\tag{35}
\]

\[
\frac{|D_{S,T}|}{|V_T|}
\ge
2^{-B}(1-\log2-o(1)).
\tag{36}
\]

Thus for all sufficiently large `T` one may take any fixed

\[
0<\delta<2^{-B}(1-\log2)
\tag{37}
\]

in (10)--(12). The anchor exposure forced by bounded architecture resources is therefore **not** orientation information contained in the same-horizon Farey field: an exact matched control can alter an arbitrarily large fraction of those exposed anchor coefficients without changing that field at all.

This directly separates two currencies that the ancestry program had to keep distinct. `FD-159`--`FD-163` price geometric cut exposure, parent load and leakage. Equation (23) shows that none of those geometric facts by itself certifies the Möbius labels on the exposed face from one Farey horizon.

## 5. Adversarial boundaries and the surviving source bridge

The construction is horizon-dependent. It does **not** produce one fixed infinite source that matches the Farey discrepancy field at infinitely many prescribed horizons, and it does not contradict the arithmetic fact that the actual inclusion-exclusion source is Möbius. In particular, `FD-009` proves that enforcing the physical divisor identity at every consecutive horizon through a cutoff is a triangular recovery of the Möbius prefix itself. The present result identifies the opposite endpoint: one complete horizon, even with its entire discrepancy function, leaves almost all squarefree orientations free.

The control is also a source-representation matched control, not a second realizable Farey point set. Equation (23) says that two squarefree-unit coefficient sources produce the same field through the exact `FD-117` source map. It does not claim that the altered coefficients arise as the inclusion-exclusion law of another reduced-rational ensemble. Therefore the conclusion is an information-boundary statement: any proof that wants to use the positive-density anchor of `FD-163` must say where its correct orientation comes from. It may use cross-horizon coherence, multiplicativity, exact divisor identities, or another source-specific arithmetic law. It may not treat same-horizon geometric exposure as if it already supplied those labels.

The result is stronger than a rank-nullity objection and avoids the infinite-precision issue emphasized in `FD-141`/`FD-142`. The observations are matched **exactly**, while the competing source remains discrete and preserves the exact squarefree support/amplitude class. No precision model is needed to create the ambiguity.

Finally, (9) must be read with `K` fixed before `T->infinity`. The theorem permits choosing a different fixed `K` for each desired accuracy `epsilon`; it does not claim a uniform estimate for an arbitrary growing `K(T)`. Such a statement would require short-interval or uniform Mertens cancellation that is deliberately not imported here.

## 6. Prior art and representation audit

The ingredients are classical or already anchored locally. The equivalence between PNT and `M(x)=o(x)`, the squarefree counting asymptotic, and Farey/Mertens transforms are standard. The floor-quotient compression itself is neighboring the floor-quotient-poset and Mertens-matrix literature already recorded around `FD-118`; modern Farey rank/discrepancy formulas also use Mertens sums. A targeted literature search found those expected themes but no theorem identifying the paired squarefree-sign shell flips above as an exact kernel of the **complete same-horizon Farey discrepancy field**. No novelty is claimed for sign balance, block-sum preservation, or floor-quotient order separately.

The representation audit is clean. The generic part is a sparse-cumulative-sampling fact: if an observable sees a cumulative source only at prescribed breakpoints, balanced sign swaps inside the complementary blocks are invisible. The arithmetic part is that PNT makes the physical Möbius signs asymptotically balanced in each fixed macroscopic block while preserving exact squarefree support. The Farey-specific part is `FD-117`/`FD-118`: the complete one-horizon discrepancy field sees **exactly** the floor-quotient breakpoints and no additional source coordinate. The architecture-specific consequence is supplied by `FD-163`, which forces a positive-density anchor face under bounded resources.

No new external theorem is load-bearing beyond anchors already present in `SOURCES.md`, so that file remains unchanged. No local clue changes disposition: the result narrows the source-information gate but does not resolve the spectral-allocation or joint nonsquarefree-occupation questions.

### Retrieval notes

- Internal inputs: the current line mandate, `FD-009`, `FD-117`, `FD-118`, `FD-163`, the current line synthesis, local clue dispositions, and existing PNT/Farey/floor-quotient source anchors.
- No open local adversarial-review sidecar had owner precedence when this investigation began.
- The exact shell-flip construction and dense-anchor consequence were derived before the external prior-art audit; the search was used to delimit novelty against classical Farey/Mertens and floor-quotient literature.
- `SOURCES.md`, clues, `mind/**`, graph artifacts, code, and experiments are unchanged.
- No computational or formalization handoff is warranted: the decisive claim is an exact finite block-balance argument plus standard asymptotics, and the remaining hard step is mathematical source coherence rather than a bounded machine subproblem.
