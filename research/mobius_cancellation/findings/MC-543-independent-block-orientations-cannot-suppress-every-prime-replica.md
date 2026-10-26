# MC-543 — Independent block orientations cannot suppress every prime replica

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`,
`NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`. The probability is over
one independent sign per balanced prime block. Prime signs within a block
are correlated. This is neither the usual independent-prime model nor a
statement about actual Möbius sums.

## Claim and the background-selection question

[MC-542](MC-542-balanced-prime-replicas-force-centered-window-energy.md)
shows that suppressing a balanced prime replica requires a large
prime-deleted background prefix. Its high-probability estimate controls
that background using a restriction on the product of older prescribed
primes. Can independently randomizing each block's overall orientation
make all replica energies small when that restriction is removed?

No. A single orientation has conditional probability at least one half
of producing the replica energy, uniformly over every fixed background.
For one infinite multiplicative source with independent block
orientations, this forces infinitely many large complete centered
energies. The blocks need no scale-separation assumption in the source
construction, beyond tending to infinity and using disjoint prime sets.
This does not exclude exceptional deterministic choices of orientations.

### Finite statement

Let \(Y\ge100\) be an integer and let
\[
 P=\{p_1<\cdots<p_{2h}\}\subset(4Y/3,5Y/3),\qquad
 b_p\in\{-1,1\},\quad h\ge1,\quad \sum_{p\in P}b_p=0.
\tag{1}
\]
Put
\[
 B(n)=\sum_{p\in P,\ p\le n}b_p,\quad
 w=p_{2h}-p_1,\quad \mathcal B_2=\sum_{n\in\mathbb Z}B(n)^2.
\tag{2}
\]
Fix **arbitrary** signs at every prime outside \(P\). For
\(\sigma\in\{-1,1\}\), set \(f_\sigma(p)=\sigma b_p\) on
\(P\), keep the other prime values fixed, extend multiplicatively to
square-free integers, set nonsquare-free values to zero, and take
\(f_\sigma(1)=1\). Thus
\(|f_\sigma(n)|=\mu(n)^2\). In particular \(|f_\sigma(3)|=1\).
There is no smallness assumption on any background sum or old-prime
product.

For any integer \(3Y\le X\le\lfloor13Y/4\rfloor\), let
\[
 I_X=\{X,\ldots,2X-1\},\quad H=\lfloor X/20\rfloor,
 \quad K=\lfloor\sqrt2H\rfloor,\quad L\in\{H,K\},
\]
\[
 S_{\sigma,L}(j)=\sum_{j<n\le j+L}f_\sigma(n),\qquad
 V_{\sigma,L}=\frac1X\sum_{j\in I_X}
       |S_{\sigma,L}(j)-\overline S_{\sigma,L}|^2.
\tag{3}
\]
Here \(\overline S_{\sigma,L}=X^{-1}\sum_{j\in I_X}S_{\sigma,L}(j)\).
Define the deterministic test
\[
 C(j)=B(\lfloor j/3\rfloor),\quad
 a_L(j)=C(j+L)-C(j),\quad E_L=\sum_j a_L(j)^2,
 \quad R_L=\lceil3w/L\rceil\le8.
\tag{4}
\]
The bound on \(R_L\) follows from \(3w<Y\) and
\(L\ge\lfloor3Y/20\rfloor\ge3Y/20-1\), for \(Y\ge100\).
Then
\[
 \boxed{\max_{\sigma=\pm1} V_{\sigma,L}
       \ge\frac{E_L}{X}
       \ge\frac{3\mathcal B_2}{R_L^2X}.}
\tag{5}
\]
Consequently a fair orientation, conditional on all other prime values,
satisfies
\[
 \boxed{\Pr_\sigma\{V_{\sigma,L}\ge E_L/X\}\ge\tfrac12.}
\tag{6}
\]
This holds for either length separately and each fixed scale; it does
not assert one orientation works for both lengths or every scale at once.
Any other fitted constant only increases the energy.

### Infinite-source statement

Let \(Y_k\to\infty\) be strictly increasing integers, and let
\(P_k,b_{k,p}\) satisfy (1) with pairwise disjoint \(P_k\).
All scales, prime sets and balanced templates are fixed in advance.
Fix arbitrary signs at all remaining primes. Choose independent fair
signs \(\sigma_k\), put
\[
 f(p)=\sigma_k b_{k,p}\quad(p\in P_k),
\tag{7}
\]
and extend as above. This defines one random multiplicative function
with exact magnitude \(\mu^2\) on all positive integers.

At \(X_k=3Y_k\), write \(V_{i,k}\) for the complete centered
energy of length \(L_1=\lfloor X_k/20\rfloor\) or
\(L_2=\lfloor\sqrt2L_1\rfloor\), and \(\mathcal B_{2,k}\)
for (2). Almost surely, **for each channel** \(i=1,2\),
\[
 \boxed{V_{i,k}\ge\frac{\mathcal B_{2,k}}{64Y_k}
                    \quad\text{for infinitely many }k.}
\tag{8}
\]
The two infinite sets need not coincide. The conclusion permits
arbitrarily large coherent backgrounds and arbitrary interactions
between the other blocks. Independence is required only of the block
orientation signs, with the templates and complement fixed beforehand.

For example, if a fixed \(\phi\in C^1([4/3,5/3];\mathbb C)\)
with \(D=\|\phi'\|_\infty>0\) has block targets
\[
 T_k=\sum_{p\in P_k}b_{k,p}\phi(p/Y_k),\qquad
 |T_k|\ge Y_k^{1/2+\delta}\quad(\delta>0)
\tag{9}
\]
for all sufficiently large \(k\), then almost surely each channel
has infinitely many scales with
\[
 V_{i,k}\ge\frac{3}{64D^2}|T_k|^2
           \ge\frac{3}{64D^2}Y_k^{1+2\delta}.
\tag{10}
\]
In particular an eventual \(X_k^{1+o(1)}\) complete-energy ceiling
has probability zero. The target in (9) is the selected block's
contribution, not necessarily the full smooth sum of \(f\).

## 1. Reversing the selected primes leaves the background fixed

Balance makes \(C\) supported in
\(J=\{3p_1,\ldots,3p_{2h}-1\}\). Both \(J\) and
\(J-L\) lie in \(I_X\), since \(L<Y/4\), their lower
endpoints exceed \(4Y-L>13Y/4\), and their upper endpoints are
below \(5Y<2X-1\). Thus
\[
 \sum_{j\in I_X}a_L(j)=0,\qquad \sum_j C(j)^2=3\mathcal B_2.
\tag{11}
\]
Every window starting in \(\operatorname{supp}a_L\) is contained
between \(4Y-L\) and \(5Y+L\). A multiple of a prime in
\(P\) in this region has multiplier three or four: multipliers
at most two are below \(10Y/3\), and those at least five exceed
\(20Y/3\). Multiplier four gives a nonsquare-free integer.
There is no product of two selected primes in the horizon \(7Y\).
Hence on the test support the exact difference is
\[
 S_{+,L}(j)-S_{-,L}(j)=2f(3)a_L(j).
\tag{12}
\]
All other prime values may be fixed adversarially; they cancel from
this difference. In particular three need not be random.

Let \(Z_\sigma=\sum_{j\in I_X}a_L(j)S_{\sigma,L}(j)\).
Equation (12) gives
\[
 Z_+-Z_-=2f(3)E_L,\qquad \max(|Z_+|,|Z_-|)\ge E_L.
\tag{13}
\]
By (11), any fitted constant vanishes from the pairing. Cauchy–Schwarz
therefore gives \(|Z_\sigma|^2\le E_LXV_{\sigma,L}\).
This proves the first inequality of (5) and the one-half bound (6).
A large background can cancel one orientation in this scalar test,
but cannot cancel both.

For completeness, compact support supplies the second inequality in
(5), even when translated pulses overlap. For \(j\in J\),
\(C(j+R_LL)=0\), so
\[
 C(j)=-\sum_{r=0}^{R_L-1}a_L(j+rL).
\]
Cauchy–Schwarz and summation over \(J\), counting each squared
difference at most \(R_L\) times, give
\(3\mathcal B_2\le R_L^2E_L\). This is the same elementary
discrete Poincaré bound as MC-542. If \(L\ge3w\), the two
pulses are disjoint and the stronger exact identity is
\(E_L=6\mathcal B_2\).

Finally summation by parts gives
\[
 T_k=-\sum_{n=p_1}^{p_{2h}-1}B(n)
       [\phi((n+1)/Y_k)-\phi(n/Y_k)],
 \qquad |T_k|^2\le\frac{w_kD^2}{Y_k^2}\mathcal B_{2,k}.
\tag{14}
\]
Since \(w_k<Y_k/3\), (8) implies (10) on its infinite set.

## 2. Extract causal observations without separating the source blocks

Choose a deterministic subsequence \(k_r\) with
\(Y_{k_{r+1}}>6Y_{k_r}\). This is possible for every sequence
in the claim. **Do not remove any of the other blocks from \(f\).**
Instead condition on all orientation signs outside this subsequence.
The remaining signs \(\sigma_{k_r}\) stay independent and fair.

The complete window sums at \(X_{k_r}=3Y_{k_r}\) involve only
integers below \(7Y_{k_r}\). Every prime in a later selected
block exceeds \(4Y_{k_{r+1}}/3>8Y_{k_r}\). Thus these energies
depend on the first \(r\) retained orientation signs and on the
already conditioned signs, but not on later retained signs. This is
the causal property needed for iteration; the window events themselves
are not asserted independent.

Fix one channel and let
\[
 A_r=\{V_{i,k_r}<\mathcal B_{2,k_r}/(64Y_{k_r})\}.
\]
After conditioning on any previous retained signs, (5)–(6) imply
\(\Pr(A_r\mid\sigma_{k_1},\ldots,\sigma_{k_{r-1}})\le1/2\).
Here \(X=3Y\) and \(R_L\le8\) give
\(E_L/X\ge\mathcal B_2/(64Y)\). Repeated conditioning yields
\[
 \Pr\left(\bigcap_{r=m}^{m+n-1}A_r
      \,\middle|\,\text{all off-subsequence signs}\right)\le2^{-n}.
\tag{15}
\]
Let \(n\to\infty\), then take the countable union over \(m\).
The probability of eventually avoiding the energy floor is zero.
Integrating over the conditioned signs proves (8). Intersecting the
two probability-one events proves the assertion for both channels.
This is an elementary conditional Borel–Cantelli argument with its
finite probability bound displayed.

The proof's sparse subsequence does not impose lacunarity on the
original prescription. For a concrete admissible family, take
\(Y_k=2^k\), beginning sufficiently far out. The proportional
prime bands are disjoint. The ordinary PNT and pigeonhole argument
in MC-538 provide ordered balanced blocks of width at most
\(Y_k^\kappa\) with \(h_k\gg Y_k^\kappa/\log Y_k\), for
any fixed \(2/3<\kappa<1\). Then
\[
 \mathcal B_{2,k}\ge(2h_k^3+h_k)/3,
 \quad V_{i,k}\gg\frac{Y_k^{3\kappa-1}}{(\log Y_k)^3}
 \quad\text{infinitely often, almost surely}.
\tag{16}
\]
The adjacent logarithmic scale ratio tends to one, and no old-prime
product bound is imposed. For the smooth targets constructed in
MC-538 one can choose \(\kappa>3/4\) and apply (9)–(10) with
any fixed \(0<\delta<2\kappa-3/2\).

## Prior art and mathematical delta

The two-point inequality in (13) is the triangle inequality, and the
iteration (15) is classical. [Durrett, Exercise 4.3.5](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf)
(MC-S92) records the conditional nonavoidance principle; the proof
above needs only repeated conditioning. No new probability inequality
or discrete Poincaré principle is claimed.

[Harper, Section 1](https://msp.org/ant/2019/13-10/ant-v13-n10-p02-s.pdf)
(MC-S88) defines the usual independent-prime Rademacher model.
Here all primes in one block share one orientation, so its moment
estimates cannot be imported. [Harper–Soundararajan–Xu, Section 2](https://arxiv.org/html/2606.29040v1#S2)
(MC-S95) supplies adjacent prior art on conditioning multiplicative
interval sums; its Steinhaus variance/concentration results do not
apply to this correlated-block ensemble. The ordinary
[PNT](https://dlmf.nist.gov/27.12) (MC-S89) supplies only the optional
block population in (16), not cancellation.

MC-542 already supplies the replica geometry, support estimate and
smooth-target transfer. The additional result is (8): independent
orientations cannot keep every complete replica energy small even
with an unrestricted fixed background and without a lacunary source
prescription. This replaces a small-background moment hypothesis by
an explicit independence hypothesis on block orientation. It neither
improves MC-542's probability tending to one at a single block under
its stronger hypotheses nor proves external novelty.

## Boundaries and validation

The disjointness of the selected prime sets is essential to specifying
independent orientations consistently. Their containing proportional
bands may overlap. The templates, locations, and complementary prime
signs must be fixed before the orientation draws. A complementary
assignment chosen in response to those draws can destroy the
conditional law used in (15); arbitrary deterministic or adaptively
coordinated cancellation remains open.

Only complete empirical energies are controlled. Sparse random
observations may miss their contribution, so this does not contradict
MC-538 or establish an optimal Möbius sampling rate. It does not
exclude deterministic dense multiplicative comparators: a probability
zero set can still contain such a construction. Nor does it prove a
large full smooth target when the complement cancels the block target.
Balance, square-free support, and a nonzero multiplier-three value
are load-bearing; removing them requires a new isolation argument.

Exact-integer checks used all 46 balanced templates on the prime sets
\(\{137,139,149,151,157,163\}\), \(\{269,277,313,331\}\), and
\(\{541,557,599,617,647,661\}\) at \(Y=100,200,400\).
For each template, 64 fixed full-prime backgrounds combined every sign
assignment at \(2,3,5,7\) with four deterministic assignments at the
remaining primes. The resulting 2,944 background/template cases checked
17,664 orientation pairs at three scales and both lengths, including
3,249,792 nonzero-test entries of (12), zero test mean, (13), centered
Cauchy–Schwarz, (5), and the rational-weight form of (14).

A separate simultaneous-family check used the disjoint prime sets
\(\{137,139,149,151,157,163\}\), \(\{167,173,179,181\}\), and
\(\{191,193,197,199,211,223\}\) at \(Y=100,115,135\), whose
proportional containing bands overlap. Exhausting all three orientation
signs and all 16 small-prime assignments checked another 384
orientation/channel pairs with the other blocks retained in the
background. A finite scalar model with past-dependent background
pairings checked the bound (15) on 10,230 histories of depths up to ten.
These checks validate finite identities and conditioning bookkeeping;
the proof, not the finite examples, establishes the almost-sure result.

No Lean verification or independent adversarial approval is asserted.
The finite two-point estimate and classical conditioning step do not
present a distinct high-value formalization target. The unresolved
research input is deterministic compatibility of background cancellation
across scales, not a missing finite probability calculation.
