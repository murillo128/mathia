# MC-214 — Higher residue moments interpolate the raw-interference Mertens barrier

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-213` shows that a centered all-residue second moment cannot control the one source-selected residue without a sharp point-evaluation loss of order `d^2` in energy, while `MC-212` shows that a diagonal-scale **separate principal energy** is already RH-equivalent for logarithmic primorial parameter `y=c log X` when `c<=1/3`. There is a quantitative interpolation between these two endpoints.

Fix an integer `k>=1`. At ambient scale `Z`, write

\[
y_Z=c\log Z,\qquad q_Z=\prod_{\ell\le y_Z}\ell,\qquad T_Z=Z-q_Z,
\]

with fixed `0<c<1/2`. For square-free `d` with `(d,q_Z)=1`, put

\[
\Phi_d=\varphi(d^2),\qquad
A_{d,a}(T_Z)
:=\sum_{\substack{n\le T_Z\\(n,q_Z)=1\\n\equiv a\pmod{d^2}}}\mu(n),
\]

for reduced residues `a mod d^2`, and decompose

\[
A_{d,a}=m_d+E_{d,a},\qquad
m_d=\frac{R_{q_Zd}(T_Z)}{\Phi_d},\qquad
\sum_a^*E_{d,a}=0,
\]

where

\[
R_Q(U):=\sum_{\substack{n\le U\\(n,Q)=1}}\mu(n).
\]

The square-defect source selects

\[
a_d\equiv-q_Z\pmod{d^2}.
\]

Define the normalized centered `2k`-moment with the units of a square by

\[
\boxed{
B_{d,k}
:=
\left(
\frac1{\Phi_d}\sum_a^*|E_{d,a}|^{2k}
\right)^{1/k},
}
\tag{1}
\]

and the dyadic shell energies

\[
\boxed{
\mathcal H_{D,k}(Z)
:=
\sum_{\substack{D<d\le2D\\\mu^2(d)=1\\(d,q_Z)=1\\d^2\le Z}}
 d\,B_{d,k},
}
\tag{2}
\]

\[
\boxed{
W_D(Z)
:=
\sum_d d\,|A_{d,a_d}(T_Z)|^2.
}
\tag{3}
\]

Suppose that for every `epsilon>0`, all sufficiently large ambient scales `Z`, and every admissible root-modulus shell `D>=y_Z`,

\[
\boxed{
W_D(Z)+\mathcal H_{D,k}(Z)
\ll_{c,k,\varepsilon} Z^{1+\varepsilon}.
}
\tag{H_{c,k}}
\]

Then

\[
\boxed{
M(X)
\ll_{c,k,\varepsilon}
X^{\beta_k(c)+\varepsilon},
\qquad
\beta_k(c)
=
\frac12+
\frac c2\max\!\left((3+2/k)c-1,0\right).
}
\tag{4}
\]

Consequently

\[
\boxed{
c\le\frac{k}{3k+2}
\quad\Longrightarrow\quad
(H_{c,k})\Longrightarrow RH.
}
\tag{5}
\]

The thresholds interpolate exactly between

\[
k=1:\ c\le\frac15,
\qquad
k=2:\ c\le\frac14,
\qquad
k=3:\ c\le\frac3{11},
\qquad
k\to\infty:\ c\uparrow\frac13.
\tag{6}
\]

Equivalently, for any fixed `c<1/3`, a sufficiently high but still **fixed** centered residue moment, together with diagonal-scale raw prescribed-residue energy, already forces the critical Mertens exponent. The required moment order is

\[
\boxed{
k\ge\frac{2c}{1-3c}}
\tag{7}
\]

(up to taking the next integer).

This is a one-way implication. RH alone is **not** asserted to imply `(H_{c,k})`, because the centered moments contain nonprincipal Dirichlet-character information not controlled by RH for the Riemann zeta function alone.

The result sharpens the surviving `MC-213` route. Replacing a centered variance by any fixed higher moment reduces the selected-residue leverage from `d^2` to `d^{2/k}`, but it does not create the signed principal/transverse anti-alignment needed by the raw coefficient. At the same time, if both the raw source coefficient and that higher centered moment are controlled uniformly across ambient scales and shells, the remaining principal mode becomes strong enough to recover Mertens cancellation below the threshold `(5)`.

No bound in `(H_{c,k})`, no improved estimate for `M(X)`, and no new zero-free region is proved here.

## 1. Sharp centered `L^{2k}` point-evaluation constant

Let `E=(E_a)_{a\in G}` be any complex vector on a finite set of size `Phi>=2` with

\[
\sum_aE_a=0.
\]

Fix one coordinate `a_0` and put

\[
B_k(E)=\left(\frac1\Phi\sum_a|E_a|^{2k}\right)^{1/k}.
\]

For fixed `E_{a_0}=z`, convexity gives the minimum possible contribution from the other `Phi-1` coordinates when all of them equal `-z/(Phi-1)`. Hence

\[
\sum_a|E_a|^{2k}
\ge
|z|^{2k}
\left(1+(\Phi-1)^{1-2k}\right).
\]

Therefore

\[
\boxed{
|E_{a_0}|^2
\le
C_{\Phi,k}\,B_k(E),
\qquad
C_{\Phi,k}
:=
\left(
\frac{\Phi}{1+(\Phi-1)^{1-2k}}
\right)^{1/k}.
}
\tag{8}
\]

The constant is sharp in the zero-sum ambient space, attained by the profile

\[
E_{a_0}=z,
\qquad
E_a=-\frac z{\Phi-1}\quad(a\ne a_0).
\]

For `k=1`, `(8)` gives exactly `C_{Phi,1}=Phi-1`, recovering the sharp `MC-213` variance leverage. For fixed `k`,

\[
C_{\Phi,k}\le\Phi^{1/k}.
\tag{9}
\]

Thus higher centered moments interpolate continuously between ordinary variance and pointwise control; they do not remove the source-coordinate tax unless the moment order becomes very large.

Applying `(8)` to each modulus in a shell gives, for the selected centered energy

\[
Z_D(Z):=\sum_d d|E_{d,a_d}|^2,
\]

the exact consequence

\[
\boxed{
Z_D(Z)
\le
\max_{d\sim D}C_{\Phi_d,k}\,\mathcal H_{D,k}(Z)
\ll_k D^{2/k}\mathcal H_{D,k}(Z).
}
\tag{10}
\]

The last inequality uses only `Phi_d<=d^2` and `d<=2D`. The exponent `2/k` is sharp for arbitrary zero-sum residue profiles at fixed `k`.

## 2. Raw plus centered moment control bounds the principal energy

Define the terminal principal energy

\[
P_D(Z)
:=
\sum_d
 d\,
\frac{|R_{q_Zd}(T_Z)|^2}{\Phi_d^2}
=
\sum_d d|m_d|^2.
\tag{11}
\]

Regard the weighted vectors over the shell as in `MC-213`. Since

\[
m_d=A_{d,a_d}-E_{d,a_d},
\]

the triangle inequality in weighted `ell^2` yields

\[
\sqrt{P_D}
\le
\sqrt{W_D}+\sqrt{Z_D}.
\tag{12}
\]

Combining `(10)`, `(12)`, and `(H_{c,k})` gives

\[
\boxed{
P_D(Z)
\ll_{c,k,\varepsilon}
Z^{1+\varepsilon}D^{2/k}.
}
\tag{13}
\]

This is the exact price paid for replacing direct principal control by a raw selected-residue estimate plus a magnitude-only centered `2k`-moment.

Because every summand in `(11)` is nonnegative, for each admissible `d\asymp D`,

\[
 d\frac{|R_{q_Zd}(T_Z)|^2}{\Phi_d^2}
\ll
Z^{1+\varepsilon}D^{2/k}.
\]

Using `Phi_d<=d^2` gives

\[
\boxed{
|R_{q_Zd}(T_Z)|
\ll_{c,k,\varepsilon}
Z^{1/2+\varepsilon}
D^{3/2+1/k}.
}
\tag{14}
\]

Compare this with the `D^{3/2}` extraction cost in `MC-212` when the principal energy itself is diagonal-scale. The centered moment contributes exactly one extra factor `D^{1/k}` in amplitude.

## 3. Ambient-scale transport converts the extra leverage into the threshold

We now repeat the exact transport mechanism of `MC-212`, with only the exponent in `(14)` changed.

Fix a large target scale `X`, put

\[
Q=q_X,
\]

and use the exact rough/smooth inverse

\[
M(X)=\sum_{e\mid Q}\mu(e)R_Q(X/e).
\tag{15}
\]

Write `e=X^alpha`, so

\[
0\le\alpha\le c+o(1),
\]

and set `U=X/e`. Choose a prime `p` with

\[
y_X<p\le2y_X.
\]

For `j=0,1`, let

\[
Z_j=U/p^j,
\qquad
q_j=q_{Z_j},
\qquad
 d_j=\frac{Q}{q_j}p.
\tag{16}
\]

Exactly as in `MC-212`, `d_j` is square-free, `(d_j,q_j)=1`,

\[
q_jd_j=Qp,
\qquad
 d_j=X^{c\alpha+o(1)},
\tag{17}
\]

and `d_j^2<=Z_j` for every fixed `c<1/2`. Thus `(14)` applies at ambient scale `Z_j` on the shell containing `d_j` and gives

\[
|R_{Qp}(T_{Z_j})|
\ll
X^{\frac{1-\alpha}{2}
+c\alpha(\frac32+\frac1k)
+\varepsilon+o(1)}.
\tag{18}
\]

The endpoint correction

\[
|R_{Qp}(Z_j)-R_{Qp}(T_{Z_j})|
\le q_j
=Z_j^{c+o(1)}
\]

is smaller than the exponent in `(18)` throughout `0<c<1/2` and `0<=alpha<=c`; this follows by checking the two endpoints of the affine difference in `alpha`.

The one-prime deletion identity

\[
R_Q(U)=R_{Qp}(U)-R_{Qp}(U/p)
\tag{19}
\]

therefore yields

\[
\boxed{
|R_Q(X/e)|
\ll
X^{\frac12+
\frac{((3+2/k)c-1)}2\alpha
+\varepsilon+o(1)}.
}
\tag{20}
\]

Finally

\[
\tau(Q)=2^{\pi(c\log X)}=X^{o(1)},
\]

so inserting `(20)` into `(15)` requires only maximizing its exponent over `0<=alpha<=c`. If `(3+2/k)c<=1`, the slope is nonpositive and the maximum is `1/2`; otherwise it occurs at `alpha=c`. This proves `(4)` and `(5)`.

## 4. What the hierarchy says about the live interference route

The result distinguishes three levels of information which can otherwise look deceptively similar.

At `k=1`, ordinary centered variance pays the full `d^2` energy leverage identified in `MC-213`. If both that variance and the raw source-selected energy were controlled at diagonal scale uniformly over shells and ambient scales, the transport above would already imply RH for `c<=1/5`.

A centered fourth moment (`k=2`) reduces the leverage to `d` and moves the forced-RH threshold to `c<=1/4`. More generally, for every fixed `c<1/3`, finitely many centered moments suffice to make the combination Mertens-complete; `(7)` gives the exact order required by this argument. The `c=1/3` principal-energy boundary of `MC-212` is recovered only in the `k->infinity` / pointwise-control limit.

This does **not** say that high centered moments are a bad target. It says what they buy and what they cost. A magnitude-only higher-moment theorem can reduce source-coordinate concentration, but it still cannot supply the negative sign in the covariance from `MC-213`. Any proof of the raw energy that reaches the selected residue only through `(8)` is therefore paying a quantified anti-concentration tax. A proof that genuinely uses principal/transverse phase can, in principle, avoid that tax entirely.

The hierarchy also supplies a falsification rule for proposed dispersion arguments. If a method claims to use a fixed `2k`-moment of centered residue errors plus the raw selected-residue estimate while remaining safely below Mertens strength, its admissible logarithmic primorial parameter must be compared with `k/(3k+2)`. Crossing that boundary means the combined hypotheses already imply the RH-scale Mertens bound through the exact ambient-scale decoder, whether or not the proof was presented as a Mertens argument.

## 5. Prior-art audit

The point-evaluation inequality `(8)` is elementary finite-dimensional convexity/Hölder geometry. No novelty is claimed for it. The ambient-scale transport and exact rough-prefix decoder are inherited from `MC-210`--`MC-212`; the new line-specific content is their quantitative composition with the full fixed-moment interpolation `(8)`--`(14)`.

Adam J. Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences*, Journal of the London Mathematical Society 112 (2025), e70293, studies centered **second-moment** progression variance for general complex sequences. It is adjacent to the `k=1` object but does not provide the source-selected raw energy or the higher centered moment hypothesis `(H_{c,k})`.

Régis de la Bretèche and Daniel Fiorilli, *Moments of moments of primes in arithmetic progressions*, Proceedings of the London Mathematical Society 127 (2023), 165--220, DOI `10.1112/plms.12542`, studies weighted even moments for prime-counting errors in arithmetic progressions, including unconditional lower-bound results and conditional distributional statements. This confirms that higher progression moments are a substantive theorem surface rather than a formal restatement of variance, but it concerns primes and a different averaging regime; it does not yield `(H_{c,k})` for the Möbius/primorial/square-modulus family.

Granville and Shao, *Bombieri--Vinogradov for multiplicative functions, and beyond the x^{1/2}-barrier*, Advances in Mathematics 350 (2019), 304--358, DOI `10.1016/j.aim.2019.04.055`, develops progression-distribution results and obstructions for multiplicative functions, explicitly separating exceptional-character effects from generic mean-value distribution. Its results are important adjacent prior art for attempts to control centered Möbius progression data, but they do not supply the fixed higher residue moments in `(2)` nor the source-prescribed raw coefficient in `(3)`.

A targeted search over higher moments in arithmetic progressions, general-sequence BDH, multiplicative-function Bombieri--Vinogradov theory, and square-modulus large-sieve literature found no theorem used here as evidence for the combined implication `(4)`--`(5)`. This is not a literature-absence or novelty claim.

## 6. Boundaries and falsification tests

- `(H_{c,k})` is a **uniform family over all sufficiently large ambient scales and all admissible root shells**. A moment estimate on one isolated scale, one shell, or a sparse subsequence does not trigger the transport proof.
- The moment order `k` is fixed independently of `X`. Allowing `k=k(X)` changes constants and uniformity and is not covered by `(4)`.
- `B_{d,k}` is the centered moment over all reduced residues. It is not a moment over moduli, characters, shifts, or ambient scales; replacing it by a different higher-moment statistic requires a new conversion theorem.
- No Gaussian or independence model is assumed. The `Z^{1+o(1)}` scale for `\mathcal H_{D,k}` is a hypothesis, not a consequence of a random model or of its literal diagonal.
- The sharp constant `(8)` is an ambient zero-sum extremum. Möbius progression profiles may satisfy additional arithmetic restrictions; any such restriction that improves the source-coordinate factor would be new positive information and would strengthen the conclusion.
- The result does not prove that raw energy, centered variance, or any higher centered moment is diagonal-scale. It only quantifies the Mertens consequence if both pieces are controlled as in `(H_{c,k})`.
- RH does not imply `(H_{c,k})` as stated. Controlling the nonprincipal character sectors generally asks for information about Dirichlet `L`-functions beyond RH for `zeta`.
- Most importantly, `(8)` uses only magnitude. A source-specific signed covariance or direct raw dispersion theorem may evade the whole hierarchy because it need not pass from a centered norm to one coordinate by Hölder/Cauchy.

## Consequence for the line

The live square-defect question is now more sharply stratified. Ordinary centered variance is only the first member of a hierarchy: a fixed `2k`-moment reduces the source-coordinate leverage to `d^{2/k}`, but for every `c<1/3` a finite moment order makes diagonal-scale **raw plus centered-moment** control Mertens-complete under the existing ambient-scale decoder.

Therefore the most genuinely distinct escape remains the one isolated by `MC-213`: control the raw source-selected coefficient through arithmetic phase/sign information rather than through magnitude-only residue anti-concentration. Higher moments are still useful diagnostics and may extend the range of any partial theorem, but they do not by themselves manufacture the required principal/transverse anti-alignment.