# MC-544 — Fixed character backgrounds cancel balanced prime replicas

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `MATCHED-CONTROL`,
`NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.
The source is a fixed character-based multiplicative control with exact
square-free magnitude. It supports both proportional-width selectors
and selectors of width \(Y^\kappa\), for every fixed
\(3/4<\kappa<1\). This is not a bound for Möbius and does not produce
a large full-source smooth sum.

## Claim: deterministic background compatibility is possible

[MC-543](MC-543-independent-block-orientations-cannot-suppress-every-prime-replica.md)
excludes eventual small replica energies for independent fair block
orientations, but leaves exceptional deterministic coordination open.
In its full proportional-band class, that exception is nonempty and
can be realized by an elementary fixed source.

Let \(\chi_4(n)\) be zero on even integers, one on \(n\equiv1\pmod4\),
and minus one on \(n\equiv3\pmod4\). Define the multiplicative function
\[
 f(2)=1,\qquad f(p)=\chi_4(p)\quad(p\text{ odd prime}),\qquad
 f(p^a)=0\quad(a\ge2),\qquad f(1)=1.
\tag{1}
\]
Then \(|f(n)|=\mu(n)^2\), and its summatory function satisfies
\[
 F(x):=\sum_{n\le x}f(n),\qquad |F(x)|\le2\sqrt x\quad(x\ge1).
\tag{2}
\]
For every integer \(X\ge1\), \(1\le L\le X\), set
\[
 I_X=\{X,\ldots,2X-1\},\quad S_L(j)=F(j+L)-F(j),\quad
 V_L(X)=\frac1X\sum_{j\in I_X}|S_L(j)-\overline S_L|^2.
\]
Here \(\overline S_L\) is the empirical mean. Uniformly in both parameters,
\[
                         \boxed{V_L(X)\le64X.}
\tag{3}
\]

Nevertheless, for every sufficiently large integer \(Y\), there is an
explicit balanced prime set
\[
 P_Y\subset(4Y/3,5Y/3),\qquad |P_Y|=2h_Y,\qquad
 b_p=f(p),\qquad \sum_{p\in P_Y}b_p=0,
\]
with
\[
 h_Y\sim\frac{Y}{24\log Y},\qquad
 T_Y:=\sum_{p\in P_Y}b_p\frac pY,\qquad
 \boxed{|T_Y|\ge h_Y/6\asymp Y/\log Y.}
\tag{4}
\]
Thus the selected targets exceed \(Y^{1/2+\delta}\) eventually for
every fixed \(0<\delta<1/2\), while both MC-543 complete centered
energies obey (3) throughout its observation band. On \(Y_k=2^k\)
the sets \(P_{Y_k}\) are disjoint, and the **same** function (1)
works at every scale. All blocks and all prime signs are deterministic.

The prime-deleted backgrounds actually pay the prefix cost identified
by MC-542 and cancel its replica pairing to relative error
\(O(\log Y/\sqrt Y)\). Consequently neither multiplicativity nor
consistency of the full-band selected targets across scales upgrades
MC-543's almost-sure obstruction to a deterministic impossibility.

## 1. The square-root bound is classical and unconditional

Put
\[
 U(x)=\sum_{n\le x}\mu(n)^2\chi_4(n),\qquad
 C_4(t)=\sum_{m\le t}\chi_4(m)\in\{0,1\}.
\]
The classical square-divisor identity gives
\[
 U(x)=\sum_{\substack{d\le\sqrt x\\d\text{ odd}}}
           \mu(d)C_4(x/d^2),\qquad |U(x)|\le\sqrt x.
\tag{5}
\]
Indeed, \(\mu(n)^2=\sum_{d^2\mid n}\mu(d)\), and
\(\chi_4(d^2m)=\chi_4(m)\) for odd \(d\), while even \(d\)
give zero. No cancellation in the outer Möbius sum is used.

Every even square-free integer has the form \(2m\) with \(m\) odd,
so repairing the character's prime-two zero as in (1) yields
\[
 F(x)=U(x)+U(x/2),\qquad
 |F(x)|\le(1+2^{-1/2})\sqrt x<2\sqrt x.
\tag{6}
\]
For \(j\in I_X\) and \(L\le X\), this gives
\(|S_L(j)|\le2(\sqrt3+\sqrt2)\sqrt X<8\sqrt X\).
Empirical centering decreases the sum of squares, proving (3).
The analogous square-divisor argument is already present in
[MC-055, Section 3](MC-055-quadratic-character-prefix-interpolation-uniformity-barrier.md).
Here the conductor is fixed at four and the local repair preserves
the magnitude on even square-free integers.

## 2. Fixed residue selectors produce large balanced block targets

Let
\[
 A_Y=\{p:4Y/3<p\le17Y/12,\ p\equiv1\pmod4\},\qquad
 D_Y=\{p:19Y/12<p<5Y/3,\ p\equiv3\pmod4\}.
\tag{7}
\]
The classical PNT in arithmetic progressions at fixed modulus four
gives \(|A_Y|,|D_Y|\sim Y/(24\log Y)\). Let
\(h_Y=\min(|A_Y|,|D_Y|)\), take the smallest \(h_Y\) primes
from each set, and let \(P_Y\) be their union. These are deterministic
selectors; no random sample or later orientation draw defines them.

Every selected prime in the lower interval has sign one, and every
selected prime in the upper interval has sign minus one. Pairing the
two lists arbitrarily shows
\[
 -T_Y=\frac1Y\sum_{r=1}^{h_Y}(p_r^- -p_r^+)>h_Y/6.
\tag{8}
\]
This proves (4). Also \((4Y/3,5Y/3)\) and
\((8Y/3,10Y/3)\) are disjoint, so the dyadic family has disjoint
prime sets, as required by MC-543.

For use in the replica test, define
\[
 B_Y(n)=\sum_{p\in P_Y,\ p\le n}b_p,\quad
 w_Y=\max P_Y-\min P_Y<Y/3,\quad
 \mathcal B_{2,Y}=\sum_{n\in\mathbb Z}B_Y(n)^2.
\]
Between the last selected positive prime and the first negative one,
\(B_Y=h_Y\), on more than \(Y/6\) integer positions. Everywhere
\(0\le B_Y\le h_Y\). Thus
\[
 \frac{Yh_Y^2}{6}<\mathcal B_{2,Y}\le w_Yh_Y^2
                                      <\frac{Yh_Y^2}{3}.
\tag{9}
\]
This is the wide-block regime allowed in MC-543 and in Section 5 of
MC-542. Section 4 supplies sublinear-width selectors as well.

## 3. One source supplies the required backgrounds at every scale

For each \(Y\), obtain \(g_Y\) from (1) by setting its prime values
to zero on \(P_Y\), leaving every other prime value unchanged.
Let \(G_Y(t)=\sum_{n\le t}g_Y(n)\) and
\(A_Y^*=\max_{0\le t\le7Y}|G_Y(t)|\).
At \(t_Y=\lfloor3Y/2\rfloor\), only the selected lower primes
have appeared, and none of their nontrivial multiples have appeared.
Hence
\[
 G_Y(t_Y)=F(t_Y)-h_Y,
 \qquad A_Y^*\ge h_Y-2\sqrt{3Y/2}.
\tag{10}
\]
Each selected prime has at most five multiples below \(7Y\).
Consequently \(|F(t)-G_Y(t)|\le10h_Y\) there, and
\[
                      A_Y^*\asymp h_Y\asymp Y/\log Y.
\tag{11}
\]
The auxiliaries \(g_Y\) differ with the removed set, but are all
restrictions of the single fixed source (1), not independently chosen
backgrounds at different scales.

The cancellation can also be seen in the exact MC-543 pairing. For
integer \(3Y\le X\le\lfloor13Y/4\rfloor\), set
\[
 H=\lfloor X/20\rfloor,\quad K=\lfloor\sqrt2 H\rfloor,
 \quad L\in\{H,K\},\qquad
 C(j)=B_Y(\lfloor j/3\rfloor),\quad a_L(j)=C(j+L)-C(j),
 \quad E_L=\sum_j a_L(j)^2.
\]
Both translated supports lie inside \(I_X\), so \(\sum_j a_L(j)=0\).
Writing \(R_L=\lceil3w_Y/L\rceil\le8\), telescoping \(C\)
along residue chains modulo \(L\) gives
\(3\mathcal B_{2,Y}\le R_L^2E_L\). In combination with (9),
\[
                         E_L\ge Yh_Y^2/128.
\tag{12}
\]
On the support of \(a_L\), windows lie between \(4Y-L\) and
\(5Y+L\). Among multiples of selected primes, only multiplier three
survives square-free support there: multipliers at most two and at
least five lie outside, and multiplier four vanishes. Since \(f(3)=-1\),
\[
 S_L(j)-[G_Y(j+L)-G_Y(j)]=-a_L(j)
                         \quad(a_L(j)\ne0).
\tag{13}
\]
This is the same physical isolation used by MC-542/543.
Put \(Z_f=\sum_{j\in I_X}a_L(j)S_L(j)\), and define
\(Z_g\) with the \(G_Y\) windows. Equations (3) and (13) imply
\[
 Z_g=E_L+Z_f,\qquad
 |Z_f|\le\sqrt{E_LXV_L(X)}\le8X\sqrt{E_L}.
\]
Thus, uniformly throughout the scale band and for both channels,
\[
              \boxed{\frac{Z_g}{E_L}
                   =1+O\!\left(\frac{\log Y}{\sqrt Y}\right).}
\tag{14}
\]
The background cancels the selected contribution \(-E_L\) to relative
error tending to zero. Its large prefix in (11) is exactly compatible
with the necessary background cost of MC-542.

## 4. Narrow balanced blocks also have compatible backgrounds

Fix \(3/4<\kappa<1\). Keep exactly the source (1), and put
\[
 W=4\lfloor Y^\kappa/40\rfloor,\qquad u=\lfloor3Y/2\rfloor.
\tag{16}
\]
For all sufficiently large integer \(Y\), select primes from
\[
 \begin{split}
 A_{Y,\kappa}&=\{p:u<p\le u+W/4,\ p\equiv1\pmod4\},\\
 D_{Y,\kappa}&=\{p:u+3W/4<p\le u+W,\ p\equiv3\pmod4\}.
 \end{split}
\tag{17}
\]
The unconditional short-interval prime number theorem in fixed
progressions gives
\[
 |A_{Y,\kappa}|,|D_{Y,\kappa}|\sim\frac{W}{8\log Y}.
\tag{18}
\]
One precise source is Thorner--Zaman, Theorem 1.1, Remark 1.2 and
the short-interval deduction in Section 1.2 of the
[author manuscript, pp. 1--3](https://arxiv.org/pdf/2108.10878v2)
(MC-S99). Take modulus four and choose a fixed
\(0<\epsilon<\kappa-7/12\); the lengths \(W/4\) eventually exceed
\(x^{7/12+\epsilon}\log x\) at both upper endpoints \(x\asymp Y\).
The weighted prime asymptotic converts to (18) because
\(\log p/\log Y\to1\) uniformly here. This stronger input is
necessary for these prescribed narrow intervals; fixed-proportion
PNT alone does not justify (18). No RH or GRH is used.

Let \(h=\min(|A_{Y,\kappa}|,|D_{Y,\kappa}|)\) and take the
smallest \(h\) primes of each class. Their union \(P\) is inside
\((4Y/3,5Y/3)\), has diameter \(w<W\), and the inherited signs
\(b_p=f(p)\) balance. Every selected positive prime precedes every
selected negative prime, with a gap greater than \(W/2\). Thus
\[
 -T_{Y,\kappa}:=-\sum_{p\in P}b_p\frac pY
       >\frac{hW}{2Y}
       \asymp_\kappa\frac{Y^{2\kappa-1}}{\log Y}.
\tag{19}
\]
The matching upper bound \(|T_{Y,\kappa}|\le hW/Y\) follows by
pairing the two lists. In particular this selected smooth target
exceeds \(Y^{1/2+\delta}\) eventually whenever
\(0<\delta<2\kappa-3/2\). The source itself remains independent
of \(Y\), \(\kappa\), and all observation draws. For each fixed
\(\kappa\), the selected sets at \(Y=2^k\) are eventually disjoint.

Write \(B(n)=\sum_{p\in P,p\le n}b_p\),
\(\mathcal B_1=\sum_n B(n)\), and
\(\mathcal B_2=\sum_n B(n)^2\). The plateau between the two
selection intervals has at least \(W/2\) integer positions. Hence
\[
 0\le B\le h,\qquad
 \mathcal B_1\le Wh,\qquad
 \frac{Wh^2}{2}\le\mathcal B_2\le Wh^2.
\tag{20}
\]
Throughout \(3Y\le X\le\lfloor13Y/4\rfloor\), for both lengths
\(L=H,K\) of Section 3, eventually \(3W\le H\le L\). The two
translated supports of
\[
 a_L(j)=B(\lfloor(j+L)/3\rfloor)-B(\lfloor j/3\rfloor)
\]
are then disjoint and contained in \(I_X\). Consequently
\[
 \sum_j a_L(j)=0,\qquad
 E_L:=\sum_j a_L(j)^2=6\mathcal B_2,\qquad
 \sum_j|a_L(j)|=6\mathcal B_1.
\tag{21}
\]
The exact replica isolation (13) still holds after zeroing precisely
these selected primes to form \(g_{Y,\kappa}\). Indeed, on the test
support the windows still lie between \(4Y-L\) and \(5Y+L\);
only multiplier three survives, and \(f(3)=-1\). Thus
\(Z_g=E_L+Z_f\) as before. The pointwise bound
\(|S_L(j)|<8\sqrt X\) and (20)--(21) give the uniform estimate
\[
 \boxed{\left|\frac{Z_g}{E_L}-1\right|
       \le\frac{16\sqrt X}{h}
       \ll_\kappa Y^{1/2-\kappa}\log Y=o(1).}
\tag{22}
\]
This uses the actual first absolute moment of the separated test;
no inference from a random-ensemble expectation is involved.

At \(t=u+W/2\), the selected prime prefix is \(h\) and none of
its composite copies has appeared, so
\(G_{Y,\kappa}(t)=F(t)-h\). Each selected prime still has at
most five multiples through \(7Y\). Since \(h\gg\sqrt Y\),
\[
 \max_{0\le t\le7Y}|G_{Y,\kappa}(t)|
       \asymp_\kappa h\asymp_\kappa Y^\kappa/\log Y.
\tag{23}
\]
Thus the full background can pay for and cancel even a narrow
balanced replica with a super-square-root selected target. Its
cost is not evidence that the full source has a large target.

## 5. What this closes, and what it does not

In MC-543's notation take \(b_{k,p}=f(p)\) on these disjoint dyadic
sets, and fix the complement to the other prime values of (1).
The deterministic orientation sequence \(\sigma_k=+1\) then retains
all targets (4) while satisfying (3) on every scale. Independently
randomizing those orientations is a different source law, to which
MC-543 still applies. There is no conflict with its probability-zero
exceptional set.

The target is selection-sensitive. For any fixed
\(\phi\in C^1([4/3,5/3])\), partial summation from (2) gives
\[
 \left|\sum_{4Y/3<n\le5Y/3}f(n)\phi(n/Y)\right|
                         \ll_\phi\sqrt Y.
\tag{15}
\]
The same bound holds uniformly on every subinterval of this band:
the two boundary terms and the variation term in partial summation
are all \(O_\phi(\sqrt Y)\). Thus it also applies to the full
narrow source sum over \((u,u+W]\) in Section 4.
For \(\phi(t)=t\), the omitted coefficients therefore cancel the
selected \(Y/\log Y\) target already in its original band. This
does not produce the large **full-source** target or dispersion sought
in the dense-scale extension of MC-538, and it supplies no sparse-sample
lower bound. It eliminates deterministic impossibility based only on
large selected balanced targets, exact square-free magnitude and
multiplicativity, including narrow selectors in Section 4. In fact
(2) gives \(D_i(X)\le16\sqrt X\) for the pair-dispersion statistic
of MC-540. This cannot meet a floor \(cX^{2\kappa-1}\) when
\(\kappa>3/4\). Narrowing the selectors therefore does not repair
the missing full-source signal. Nor do (19)--(22) exclude constructions
that prescribe signs independently of this fixed character.

The control agrees with \(\chi_4\) at every odd prime. It therefore
does not model the absence of correlation with fixed Dirichlet characters
that an arithmetic Möbius argument may require. Its prime values also
do not obey \(\mu(p)=-1\). These are genuine extra discriminators,
not consequences of the hypotheses checked here. A useful next
implication must retain a full-source target, constrain the selectors,
or impose an additional arithmetic hypothesis excluding this control.

## Prior art, mathematical delta and validation

Character periodicity and multiplicativity are classical
([NIST DLMF §27.8](https://dlmf.nist.gov/27.8)). The square-divisor
argument in (5) is the elementary fixed-conductor specialization of
classical square-free character-sum methods; see MC-055 and
[Munsch, *Character sums over squarefree and squarefull numbers*](https://doi.org/10.1007/s00013-014-0658-9)
(MC-S38). No moving-conductor estimate from that paper is needed.
The broad selectors use the fixed-modulus PNT in progressions
([Kedlaya, Theorem 4.12](https://kskedlaya.org/ant/chap-primes-in-ap.html),
MC-S98). The narrow selectors additionally use the unconditional
short-interval specialization of Thorner--Zaman recorded in MC-S99.
No moving-modulus uniformity or GRH assumption enters.

The character cancellation itself is prior art, and the two-interval
selection is elementary. The mathematical delta is the explicit
compatible family (1), (7), (10), (14), which settles the deterministic
background-existence question left by MC-542/543. Equations (16)--(23)
extend the same compatible source to the sublinear-width regime with
super-square-root selected targets. They remove width alone as a way
to exclude the character control; the missing full-source or
additional-arithmetic condition remains. The narrow extension combines
a classical prime-population theorem with the same replica identity;
no new prime-distribution or cancellation mechanism or external
novelty is claimed.

Exact-integer validation checked (6), exact square-free magnitude and
\(F(n)^2\le4n\) at all 114,688 prefixes; the square-divisor formula at
4,096 prefixes; and multiplicativity on 54,635 coprime pairs with both
entries below 300. At \(Y=256,512,\ldots,16384\), the construction (7)
was checked at \(X=3Y,\lfloor25Y/8\rfloor,\lfloor13Y/4\rfloor\)
and both lengths: 42 channel/scale cases checked balance, (8)–(10),
zero test mean, (12), (14)'s finite Cauchy–Schwarz bound, and 161,660
nonzero-test entries of (13).

For the narrow construction, an additional exact-integer sieve checked
the square-root prefix bound through 1,835,008. With
\(\kappa=4/5,7/8\) and \(Y=2^{10},\ldots,2^{18}\), thirteen
blocks had nonempty selections in both residue classes. Integer roots
computed (16) without floating-point endpoint decisions. Seventy-eight
channel/scale cases checked (19)--(21), the deletion identity at
\(u+W/2\), \(Z_g=E_L+Z_f\), and the squared finite bound
\(h^2 Z_f^2\le256XE_L^2\) from (22); they included 578,952
nonzero-test entries of (13). The finite relative error need not be
small when \(h\) is small. These checks audit identities and integer
endpoints; the cited prime theorems and displayed proofs establish the
asymptotic statements. No Lean verification or independent adversarial
approval is asserted. The classical decomposition and explicit
selector do not identify a separate high-value formalization target.
