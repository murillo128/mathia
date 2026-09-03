# WI-113 — Sedunova's logarithmic Bombieri--Vinogradov theorem pushes full-packed near-nullity to the log-squared endpoint

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It strictly strengthens WI-112's square-root/polylogarithmic full-packing obstruction by replacing the classical `log^5` bookkeeping there with Sedunova's published maximal Bombieri--Vinogradov theorem. For every fixed `B>2`, the WI-111 quotient-character construction can be driven to a near-null sector of dimension

\[
\ell-1\asymp \frac{\sqrt p}{(\log p)^B},
\]

with relative singular scale

\[
O\!\left(p^{-1/4}(\log p)^{-(B-1)/2}\right).
\]

Consequently, for every fixed `C>2`, arbitrary global linear processing cannot retain both fixed conditioning and fixed normalized transmission merely by deleting

\[
O\!\left(\frac{\sqrt p}{(\log p)^C}\right)
\]

source directions. WI-112 obtained the same conclusion only for `C>5`. The threshold `2` is also the exact boundary of this **black-box Sedunova + Markov selection argument**: at `B=2` the theorem no longer forces the bad-modulus proportion inside the required residue family to vanish.

## 1. The load-bearing published theorem has exactly the needed maximal interface

Alisa Sedunova, **A logarithmic improvement in the Bombieri--Vinogradov theorem**, *Journal de Théorie des Nombres de Bordeaux* 31 (2019), 635--651, DOI `10.5802/jtnb.1098`, arXiv:1705.06660, proves in Theorem 1.2 the following maximal form. For every fixed `A>2` and

\[
Q\le \frac{x^{1/2}}{(\log x)^A},
\]

one has

\[
\boxed{
\sum_{q\le Q}
\max_{2\le y\le x}
\max_{(a,q)=1}
\left|\psi(y;q,a)-\frac{y}{\varphi(q)}\right|
\ll_A
\frac{x}{(\log x)^{A-2}}.
}
\tag{1}
\]

The implied constant is ineffective, but that is irrelevant for the existence argument below. The two maxima in (1) are important: the source and target residue classes may be chosen after the modulus, and the same good modulus controls all four interval endpoints used in WI-111/WI-112.

Sedunova explicitly improves the previous Dress--Iwaniec--Tenenbaum logarithmic loss from `A-5/2` to `A-2`. WI-112 deliberately did not import this sharper theorem; it used instead a classical maximal character-sum form with a `log^5` loss and recorded Sedunova as the natural next endpoint audit. The present finding performs that translation directly from Theorem 1.2 rather than inferring it from the paper's abstract or from a secondary summary.

## 2. The good-modulus selection now works for every `B>2`

Fix

\[
B>2
\tag{2}
\]

and let `X` tend to infinity. Set

\[
Q_0=\frac{\sqrt X}{4(\log X)^B}.
\tag{3}
\]

Apply (1) with `x=2X`, `A=B`, and `Q=2Q_0`. For all sufficiently large `X`,

\[
2Q_0
=\frac{\sqrt X}{2(\log X)^B}
\le
\frac{\sqrt{2X}}{(\log(2X))^B},
\tag{4}
\]

so Sedunova gives

\[
\sum_{M\le2Q_0} E^*(2X,M)
\ll_B \frac{X}{(\log X)^{B-2}},
\tag{5}
\]

where

\[
E^*(2X,M)=
\max_{2\le y\le2X}
\max_{(a,M)=1}
\left|\psi(y;M,a)-\frac{y}{\varphi(M)}\right|.
\tag{6}
\]

Restrict to the same arithmetic family as WI-112,

\[
\mathcal M=
\{M:Q_0\le M\le2Q_0,\ M\equiv2\pmod4\}.
\tag{7}
\]

It has `asymp Q_0` members. Fix a sufficiently small absolute `eta>0`, for example any `eta<1/100`, and call `M` bad if

\[
E^*(2X,M)>\eta\frac{X}{Q_0}.
\tag{8}
\]

Markov's inequality and (5) imply

\[
\#\{M\in\mathcal M:M\text{ bad}\}
\ll_{B,\eta}
\frac{Q_0}{(\log X)^{B-2}}
=o(Q_0).
\tag{9}
\]

Because `B>2`, a good modulus exists for every sufficiently large `X`. Write

\[
M=2\ell.
\tag{10}
\]

The congruence `M=2 mod 4` makes `ell` odd, and from (3), (7), (10),

\[
\boxed{
\ell\asymp Q_0
\asymp\frac{\sqrt X}{(\log X)^B}.
}
\tag{11}
\]

The strict inequality `B>2` is load-bearing only in (9). At `B=2`, this black-box argument yields merely `O(Q_0)` bad moduli, the same order as the entire candidate family (7), and the ineffective constant gives no way to force one survivor. Thus Sedunova's theorem by itself reaches every logarithmic exponent strictly larger than two, but not the endpoint two.

## 3. One good modulus supplies the same source and nearby targets as WI-112

Use the fixed separated intervals

\[
I_s=[X,1.05X],
\qquad
I_t=[1.10X,1.15X],
\tag{12}
\]

and the residue classes

\[
a_s=1\pmod{2\ell},
\qquad
a_t=\ell+2\pmod{2\ell}.
\tag{13}
\]

Since `ell` is odd,

\[
\gcd(\ell+2,2\ell)=1.
\tag{14}
\]

For a good modulus, the difference of the two endpoint estimates in (6) gives, in either interval and either required residue class,

\[
\psi(bX;M,a)-\psi(aX;M,a)
\ge
\frac{(b-a)X}{\varphi(M)}
-2\eta\frac{X}{Q_0}.
\tag{15}
\]

Here `b-a=0.05`, while `M<=2Q_0` and hence `phi(M)<=2Q_0`. Therefore the main term in (15) is at least

\[
\frac{X}{40Q_0}.
\tag{16}
\]

Choosing `eta<1/80` makes (15) positive with a fixed margin. Prime powers of exponent at least two contribute only

\[
O(\sqrt X\log X),
\tag{17}
\]

whereas

\[
\frac{X}{Q_0}\asymp \sqrt X(\log X)^B,
\tag{18}
\]

so (17) is negligible for the present `B>2`. Consequently there is an actual source prime

\[
p\in I_s,
\qquad p\equiv1\pmod{2\ell},
\tag{19}
\]

and the target interval contains

\[
J\gg_B\frac{X}{Q_0\log X}
\tag{20}
\]

actual primes with

\[
q\equiv\ell+2\pmod{2\ell}.
\tag{21}
\]

Choose two consecutive primes `q_1<q_2` from this target set. Pigeonholing inside the fixed-length interval gives

\[
\boxed{
\Delta:=q_2-q_1
\ll_B Q_0\log X
\asymp
\frac{\sqrt X}{(\log X)^{B-1}}.
}
\tag{22}
\]

The interval separation also gives

\[
p<q_i<\frac43p.
\tag{23}
\]

Thus every arithmetic hypothesis used by WI-111's exact common-center/full-packing construction is recovered, with the same congruence pattern but with `ell` at the improved scale (11).

## 4. The exact quotient-character geometry then propagates unchanged

WI-111 proves that the congruences (19), (21) permit one common observation length `N` for which both `(p,q_i,N)` are genuinely positive-defect exact full-packed interactions. Writing

\[
G_i=(U_p^{(N)})^*U_{q_i}^{(N)},
\qquad
K_i=\ker G_i^*,
\tag{24}
\]

each `K_i` contains an explicit `(ell-1)`-dimensional quotient-character subspace `W_i`. For suitable orthonormal bases `X_i`, the cross Gram is exactly

\[
X_1^*X_2
=\sqrt{\frac{t_2}{t_1}}I_{\ell-1},
\qquad
t_i=2p-q_i.
\tag{25}
\]

Hence every unit vector in either `W_i` is within squared distance

\[
\operatorname{dist}(x,K_j)^2
\le
\frac{\Delta}{t_1}
\le
\frac{3\Delta}{2p}
\tag{26}
\]

of the other kernel. This step is exact finite linear algebra and is not altered by the stronger prime-distribution input.

Allow arbitrary target-local right processing

\[
C_i:E_i\to\mathbf C^{q_i-1},
\qquad
B_{\rm op}=[\,G_1C_1\;G_2C_2\,].
\tag{27}
\]

The Courant--Fischer argument of WI-111/WI-112 therefore gives

\[
\frac{\sigma_{p-\ell+1}(B_{\rm op})}
{\sigma_1(B_{\rm op})}
\le
\sqrt{\frac{3\Delta}{2p}}.
\tag{28}
\]

Using `p asy X` together with (11) and (22),

\[
\boxed{
\ell-1
\asymp
\frac{\sqrt p}{(\log p)^B},
}
\tag{29}
\]

and

\[
\boxed{
\frac{\sigma_{p-\ell+1}(B_{\rm op})}
{\sigma_1(B_{\rm op})}
\ll_B
p^{-1/4}(\log p)^{-(B-1)/2}
\longrightarrow0.
}
\tag{30}
\]

Thus Sedunova's logarithmic saving does not merely improve a counting constant: it enlarges the explicit high-multiplicity near-null sector all the way to square-root dimension with only `log^{2+epsilon}` loss, for arbitrary fixed positive `epsilon`.

## 5. Linear rescue by low-codimension deletion is therefore closed for every `C>2`

Retain WI-110/WI-111's scale-sensitive formulation. For arbitrary further linear processing

\[
A=L B_{\rm op} S,
\tag{31}
\]

define at each retained source index `k`

\[
r_k(A)=\frac{\sigma_k(A)}{\sigma_1(A)},
\qquad
\tau_{B_{\rm op}}(L,S)
=\frac{\sigma_1(A)}
{\|L\|_2\sigma_1(B_{\rm op})\|S\|_2}.
\tag{32}
\]

The singular-value ideal property gives

\[
\boxed{
r_k(A)\tau_{B_{\rm op}}(L,S)
\le
\frac{\sigma_k(B_{\rm op})}{\sigma_1(B_{\rm op})}.}
\tag{33}
\]

Suppose a proposed rescue deletes `d(p)` source dimensions. If

\[
d(p)=o\!\left(
\frac{\sqrt p}{(\log p)^B}
\right),
\tag{34}
\]

then eventually the retained index still reaches the near-null sector in (29), and (30), (33) force

\[
\boxed{
r_k(A)\tau_{B_{\rm op}}(L,S)
\ll_B
p^{-1/4}(\log p)^{-(B-1)/2}
\to0.}
\tag{35}
\]

Now fix any

\[
C>2.
\tag{36}
\]

Choose `B` with

\[
2<B<C.
\tag{37}
\]

Then

\[
O\!\left(\frac{\sqrt p}{(\log p)^C}\right)
=o\!\left(\frac{\sqrt p}{(\log p)^B}\right),
\tag{38}
\]

so every arbitrary linear pre/post-processing rule deleting at most the left-hand scale in (38) must lose either a fixed relative singular gap or a fixed normalized transmission fraction on this exact full-packed family.

Equivalently, for every fixed `epsilon>0`, deletion of order

\[
O\!\left(\frac{\sqrt p}{(\log p)^{2+\epsilon}}
\right)
\tag{39}
\]

is still insufficient. This strictly strengthens WI-112's `5+epsilon` logarithmic threshold.

## 6. Boundary, prior art, and no-overclaim

The improvement is a direct literature-backed consequence of Sedunova's Theorem 1.2 combined with Mathia's already-persisted exact geometry in WI-111/WI-112. No new prime-distribution theorem is claimed. The novelty audit therefore classifies the load-bearing analytic input as established prior art and the `C>2` full-packing consequence as a new exact specialization within the present obstruction chain, with no priority claim.

Sedunova's paper states that its `A-2` logarithmic exponent improves the earlier Dress--Iwaniec--Tenenbaum `A-5/2` form. A targeted audit of later general Bombieri--Vinogradov refinements through 2026 found many specialized variants (short intervals, special moduli, nilsequence twists, simultaneous congruences), but did not locate a later published theorem with the same unrestricted `max_y max_a` interface and a smaller fixed logarithmic loss than Sedunova's `2`. This negative search is not a claim that such a theorem cannot exist.

The present argument does **not** reach `C=2`, let alone deletion of order `sqrt(p)`. Equation (9) shows exactly why: the black-box mean bound must beat the cardinality of the candidate modulus family by a factor tending to infinity. At `B=2`, Sedunova's theorem gives no such factor. Passing that boundary would require a stronger averaged error theorem, a structured selection argument that uses more than Markov on the unrestricted modulus sum, or additional arithmetic information about the specific `M=2 mod 4` family.

Nothing here improves the unconditional zeta simple-critical proportion, identifies the uncertified zero complement, or asserts positive analytic density of the synchronized full-packed windows. As in WI-105--WI-112, this is a uniform finite-window obstruction inside the auxiliary Ramanujan/full-packing pathway. Positive slack away from full packing, nonlinear information, zeta-specific arithmetic normalization, or an operator changed before this compression remain outside the theorem.

## 7. Program consequence

WI-112 left the logarithmic thinning in its square-root-scale obstruction as an explicitly arithmetic frontier. Sedunova removes three logarithmic powers from that frontier immediately: the known exact full-packed near-null sector can be forced at every scale

\[
\frac{\sqrt p}{(\log p)^{2+\epsilon}},
\qquad \epsilon>0,
\tag{40}
\]

rather than only `sqrt(p)/log^{5+epsilon} p`.

This also isolates the next honest endpoint. Further optimization of the already-exact quotient-character, principal-angle, Courant--Fischer, or conditioning/transmission steps cannot improve the exponent `2`; it now comes entirely from the prime-distribution selection theorem. A meaningful next attack must either lower the logarithmic loss in the relevant maximal Bombieri--Vinogradov interface, exploit the residue family `M=2 mod 4` more efficiently than the unrestricted Markov selection, or supply a different prime-selection mechanism. Within the current black-box theorem, the log-squared boundary is exact.