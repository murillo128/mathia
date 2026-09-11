# WP-258 — Free-Fock gauge determinants recover the Gamma shape only at the normalized Fock boundary, not at the Weil half-density boundary

**Status:** `EXACT-DERIVED + FREE-PRIME-FOCK + GAUGE-NUMBER + GIBBS-WEIGHTED-SPECTRAL-ZETA + LERCH-TRANSCENDENT + HURWITZ-GAMMA-BOUNDARY + ARCHIMEDEAN-CANDIDATE + TEMPERATURE-MISMATCH + SCALAR-CLOCK-RIGIDITY + MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

`WP-256` shows that the canonical free-prime Fock system contains a source-defined positive operator with the exact finite-place half-density

\[
P_{\rm simp}HN^{-1}e^{-H/2}e_w
=\frac{\Lambda(n(w))}{\sqrt{n(w)}}e_w.
\]

`WP-257` then separates the one-particle arithmetic boundary `beta=1` from the normalized free-Fock equilibrium boundary `beta=beta_*>1`, where the prime zeta function satisfies `P(beta_*)=1`.

The remaining natural question is whether the *same* free-Fock source also contains the missing archimedean Gamma factor. It has an obvious candidate: the canonical gauge/word-number operator `N`, whose multiplicity-one spectral zeta would be a Hurwitz zeta and whose zeta-regularized determinant therefore produces a Gamma function.

That idea is mathematically real but lands at the wrong thermodynamic boundary. On the actual prime Fock space, every positive length eigenspace of `N` is infinite-dimensional, so `N` has no ordinary spectral zeta. Weighting by the canonical arithmetic Gibbs factor gives instead

\[
\mathcal Z_{\beta}(u,z)
:=\operatorname{Tr}\!\left(e^{-\beta H}(N+z)^{-u}\right)
=\sum_{m\ge0}P(\beta)^m(m+z)^{-u}.
\]

For `beta>beta_*` this is the Lerch transcendent

\[
\Phi(P(\beta),u,z).
\]

Exactly at `beta=beta_*`, the length masses become one and the weighted spectral zeta becomes the Hurwitz zeta

\[
\mathcal Z_{\beta_*}(u,z)=\zeta_H(u,z).
\]

Consequently the zeta-regularized inverse determinant of the scaled gauge operator `c(N+z)` is

\[
\det_{\zeta,\beta_*}(c(N+z))^{-1}
=c^{z-1/2}\frac{\Gamma(z)}{\sqrt{2\pi}}.
\]

Setting `z=s/2` and, if an external real-place normalization supplies `c=1/pi`, this is

\[
\frac1{\sqrt2}\,\pi^{-s/2}\Gamma(s/2),
\]

the Riemann archimedean factor up to an `s`-independent constant.

But at precisely this boundary the finite carrier is

\[
P_{\rm simp}HN^{-1}e^{-\beta_*H/2}e_w
=\Lambda(n(w))n(w)^{-\beta_*/2}e_w,
\]

not `Lambda(n)/sqrt(n)`. Conversely, at `beta=1` the finite Weil coefficient is exact but the one-letter Gibbs mass `P(1)` diverges, so the canonical Gibbs-weighted gauge spectral zeta is not even defined on the first length sector.

Thus the same free-Fock `(H,N)` geometry exposes **both** a finite arithmetic carrier and a natural Gamma-shaped determinant, but its two exact target features occur at incompatible source parameters:

\[
\boxed{
\text{finite Weil half-density: }\beta=1,
\qquad
\text{Hurwitz/Gamma gauge boundary: }\beta=\beta_*>1.
}
\]

The mismatch is invariant under scalar rescaling of the arithmetic clock. It is therefore a genuine obstruction to the most canonical attempt to obtain both finite and archimedean pieces from one same-temperature Gibbs/gauge construction. It does not rule out a different source-derived archimedean trace, correspondence, quotient, or non-Gibbs regularization. It also does not address the still-missing polar factor or the Weil sign.

## 1. The actual Fock gauge operator has infinite multiplicity

Retain the free prime Fock space of `WP-256`,

\[
\mathcal F
=\mathbb C\Omega\oplus\bigoplus_{m\ge1}\mathcal K^{\otimes m},
\qquad
\mathcal K=\ell^2(\mathbb P),
\]

with arithmetic Hamiltonian and gauge number

\[
He_w=(\log n(w))e_w,
\qquad
Ne_w=|w|e_w.
\tag{1}
\]

The formal multiplicity-one operator with spectrum `0,1,2,...` would have shifted spectral zeta

\[
\sum_{m\ge0}(m+z)^{-u}=\zeta_H(u,z).
\tag{2}
\]

But that is **not** the ordinary spectral zeta of `N` on `mathcal F`. For every `m>=1`,

\[
\dim \mathcal K^{\otimes m}=\infty,
\tag{3}
\]

so for every `z>0` and every complex `u`,

\[
\operatorname{Tr}(N+z)^{-u}=\infty
\tag{4}
\]

whenever the trace is interpreted on the actual Fock Hilbert space. The obstruction is already the infinite multiplicity of the length-one eigenspace.

Therefore a bare statement that "the Fock number operator has determinant Gamma" silently replaces the actual Fock trace by a multiplicity-one length trace. Such a replacement may be useful if an independent quotient or radial trace forces it, but it is additional structure and is not inherited from the ordinary Fock representation.

## 2. The canonical arithmetic weight turns the length zeta into a Lerch transcendent

The source already supplies a distinguished way to reduce the infinite multiplicities: weight them by the arithmetic Gibbs factor. For `beta>1`, let

\[
P(\beta)=\sum_p p^{-\beta}
\tag{5}
\]

be the prime zeta function. On the length-`m` sector,

\[
\begin{aligned}
\operatorname{Tr}_{\mathcal K^{\otimes m}}(e^{-\beta H})
&=\sum_{p_1,\ldots,p_m}(p_1\cdots p_m)^{-\beta}\\
&=P(\beta)^m.
\end{aligned}
\tag{6}
\]

For `z>0`, define the Gibbs-weighted gauge spectral zeta whenever the trace converges,

\[
\mathcal Z_\beta(u,z)
:=\operatorname{Tr}\!\left(e^{-\beta H}(N+z)^{-u}\right).
\tag{7}
\]

Using the joint diagonalization of `H` and `N`, equation (6) gives

\[
\boxed{
\mathcal Z_\beta(u,z)
=\sum_{m\ge0}\frac{P(\beta)^m}{(m+z)^u}.
}
\tag{8}
\]

If `beta>beta_*`, where `P(beta_*)=1`, put

\[
q=P(\beta)\in(0,1).
\tag{9}
\]

Then (8) converges absolutely for every `u` and is exactly Lerch's transcendent,

\[
\boxed{
\mathcal Z_\beta(u,z)=\Phi(q,u,z).
}
\tag{10}
\]

This identification is classical special-function theory: DLMF §25.14 defines

\[
\Phi(q,u,z)=\sum_{m\ge0}q^m(m+z)^{-u},
\]

and records `Phi(1,u,z)=zeta_H(u,z)` in its domain and by continuation.

For `1<beta<beta_*`, one has `P(beta)>1`, so the factor `P(beta)^m` grows exponentially and (8) diverges for every fixed `u`; polynomial length damping cannot overcome the Fock growth. For `beta<=1`, already the one-letter Gibbs trace is infinite. Thus the canonical weighted gauge zeta has a sharp boundary at the same `beta_*` found in `WP-257`.

## 3. The Gamma function appears exactly when every length has equal weighted mass

At the boundary

\[
P(\beta_*)=1,
\tag{11}
\]

equation (8) becomes, for `Re(u)>1`,

\[
\boxed{
\mathcal Z_{\beta_*}(u,z)
=\sum_{m\ge0}(m+z)^{-u}
=\zeta_H(u,z).
}
\tag{12}
\]

This equality has a simple geometric meaning: the total Gibbs mass of every fixed word-length sector is exactly one. The prime degrees of freedom disappear from the weighted *length* multiplicity only at the normalized Fock packing threshold.

The Hurwitz values at zero are classical:

\[
\zeta_H(0,z)=\frac12-z,
\tag{13}
\]

and Lerch's formula gives

\[
\zeta_H'(0,z)
=\log\Gamma(z)-\frac12\log(2\pi).
\tag{14}
\]

The latter is DLMF §25.11(vi), equation 25.11.18.

For a positive scale `c`, the zeta function of the scaled gauge operator at this weighted boundary is

\[
\mathcal Z^{(c)}_{\beta_*}(u,z)
=c^{-u}\zeta_H(u,z).
\tag{15}
\]

Therefore the corresponding zeta-regularized determinant is

\[
\begin{aligned}
\det_{\zeta,\beta_*}(c(N+z))
&:=\exp\!\left(-\partial_u\mathcal Z^{(c)}_{\beta_*}(0,z)\right)\\
&=c^{1/2-z}\frac{\sqrt{2\pi}}{\Gamma(z)}.
\end{aligned}
\tag{16}
\]

Equivalently,

\[
\boxed{
\det_{\zeta,\beta_*}(c(N+z))^{-1}
=c^{z-1/2}\frac{\Gamma(z)}{\sqrt{2\pi}}.
}
\tag{17}
\]

This is an exact Gamma-shaped archimedean object coming from the canonical Fock gauge, after the canonical arithmetic weight has collapsed the length multiplicities to one.

Now set

\[
z=\frac s2.
\tag{18}
\]

If a real-place normalization independently supplies

\[
c=\frac1\pi,
\tag{19}
\]

then (17) gives

\[
\boxed{
\det_{\zeta,\beta_*}\!\left(\pi^{-1}(N+s/2)\right)^{-1}
=\frac1{\sqrt2}\pi^{-s/2}\Gamma(s/2).
}
\tag{20}
\]

The constant `1/sqrt(2)` is independent of `s`, so it disappears from logarithmic derivatives. In particular the logarithmic derivative of (20) is exactly

\[
\frac12\left(\psi(s/2)-\log\pi\right),
\tag{21}
\]

the Gamma-factor contribution associated with `pi^{-s/2}Gamma(s/2)`.

Equation (20) is a genuine positive intermediate identification at the level of scalar spectral determinant provenance. It is **not** yet a positivity theorem for the Weil quadratic form, and the scale `1/pi` is not fixed by the abstract prime Fock gauge itself. A self-dual real Fourier normalization can explain `pi`, but that is precisely additional archimedean structure that the free prime Fock system has not derived internally.

## 4. Away from `q=1`, the gauge determinant is not an ordinary Gamma factor

The special role of `beta_*` is stronger than merely recognizing a familiar formula at one point. For `0<q<1`, define

\[
D_q(z)
:=\exp\!\left(-\partial_u\Phi(q,u,z)|_{u=0}\right).
\tag{22}
\]

Absolute convergence permits termwise differentiation, giving

\[
\log D_q(z)
=\sum_{m\ge0}q^m\log(m+z)
\tag{23}
\]

and hence

\[
\frac{d}{dz}\log D_q(z)
=\sum_{m\ge0}\frac{q^m}{m+z}.
\tag{24}
\]

As a meromorphic function of `z`, the right side has a simple pole at every `z=-m` with residue `q^m`.

By contrast, the logarithmic derivative of `Gamma(z)` has equal-magnitude residue at every nonpositive integer. Multiplying by an exponential `C exp(az)` or rescaling `N+z` by a constant changes only an additive constant or the pole locations; it cannot turn the sequence of residues

\[
1,q,q^2,q^3,\ldots
\tag{25}
\]

into a constant sequence unless

\[
\boxed{q=1.}
\tag{26}
\]

Thus within this canonical Gibbs-weighted gauge-zeta family, the ordinary Gamma divisor is not available anywhere in the normal Gibbs region `beta>beta_*`. It occurs only at the boundary `P(beta)=1`, where the length masses flatten.

This is also why an arbitrary rescaling of the gauge operator `N` cannot move the Gamma boundary: it alters spectral units but not the length-sector weights `P(beta)^m`.

## 5. The finite and archimedean target pieces demand incompatible temperatures

The same free-Fock source gives, for any `beta>0`, the simple-spectrum mean-energy carrier from `WP-257`,

\[
T_\beta
:=P_{\rm simp}HN^{-1}e^{-\beta H/2},
\tag{27}
\]

with

\[
T_\beta e_w
=\Lambda(n(w))n(w)^{-\beta/2}e_w.
\tag{28}
\]

The exact finite Weil half-density requires

\[
\boxed{\beta=1.}
\tag{29}
\]

At this value,

\[
P(1)=\sum_p\frac1p=\infty.
\tag{30}
\]

Consequently even the length-one term of (7) is infinite:

\[
\operatorname{Tr}_{\mathcal K}
\!\left(e^{-H}(N+z)^{-u}\right)
=(1+z)^{-u}\sum_p\frac1p
=\infty.
\tag{31}
\]

So the same canonical Gibbs-weighted gauge determinant cannot be formed at the parameter where the finite coefficient is correct.

Conversely, at the unique parameter where the gauge length spectrum becomes Hurwitz,

\[
\boxed{\beta=\beta_*,\qquad P(\beta_*)=1,}
\tag{32}
\]

the finite carrier is

\[
T_{\beta_*}e_w
=\Lambda(n(w))n(w)^{-\beta_*/2}e_w,
\tag{33}
\]

with

\[
\frac{\beta_*}{2}
=0.6997166643\ldots\ne\frac12.
\tag{34}
\]

Therefore

\[
\boxed{
\begin{array}{c}
\text{source-exact finite half-density}\iff\beta=1,\\[2mm]
\text{source-exact Hurwitz/Gamma gauge boundary}\iff\beta=\beta_*,
\end{array}
\qquad
1<\beta_*.
}
\tag{35}
\]

This is the central incompatibility.

## 6. Scalar rescaling of the arithmetic clock cannot align the two conditions

As in `WP-257`, rescale the arithmetic Hamiltonian by

\[
H_c=cH,
\qquad c>0.
\tag{36}
\]

The one-letter partition sum at inverse temperature `beta` becomes

\[
P(c\beta).
\tag{37}
\]

The Gamma/Hurwitz gauge condition is therefore

\[
P(c\beta)=1
\quad\Longleftrightarrow\quad
c\beta=\beta_*.
\tag{38}
\]

Meanwhile the finite half-density has exponent `c beta/2`, so exact Weil scaling requires

\[
c\beta=1.
\tag{39}
\]

Equations (38) and (39) are incompatible because `beta_*>1`:

\[
\boxed{
\text{Gamma gauge boundary: }c\beta=\beta_*,
\qquad
\text{finite Weil half-density: }c\beta=1.
}
\tag{40}
\]

Thus the obstruction is invariant under the arbitrary choice of arithmetic time unit. One cannot fix it by declaring a different normalization of `H`.

An independent scale on `N` can supply the `pi` in (20), but it does not change (38), because the condition `q=1` is a statement about weighted multiplicities, not about the spacing of the length spectrum.

## 7. Aggressive controls and exact boundary of the negative result

### Multiplicity-one gauge replacement

One may simply replace the actual Fock gauge sector by an auxiliary Hilbert space with one basis vector for each length. Its spectral zeta is Hurwitz by construction and therefore its determinant is Gamma at every stage.

That is a valid classical spectral model, but it is not a consequence of the ordinary Fock trace: equations (3)--(4) show that the actual multiplicities are infinite. The canonical arithmetic Gibbs weight makes the multiplicity-one reduction exact only when `P(beta)=1`. Any other quotient, radial vector, conditional expectation, or trace that produces one copy per length at `beta=1` needs an independent source-selection theorem. This finding does not rule such a theorem out.

### Simple-spectrum restriction

Because `WP-256` uses `P_simp`, one might restrict the gauge trace to the simple energy sectors. At length `k`, the Gibbs mass is then

\[
\sum_p p^{-k\beta}=P(k\beta).
\tag{41}
\]

At the required `beta=1`, the `k=1` mass is still `P(1)=infinity`. Thus the most immediate source-aligned restriction does not produce a finite gauge zeta either. Removing the first length sector or assigning it a finite part would be an additional regularization whose geometric origin would have to be proved.

### Different thermodynamic weights

Nothing here proves that every possible positive or semifinite weight on the free Fock algebra has the same obstruction. A non-Gibbs weight, a modular weight in a different von Neumann completion, or an independently derived finite--archimedean coupling may alter the effective length multiplicities. Such a proposal must derive its weights before reading off the Gamma factor and must still reproduce the finite coefficient and Weil sign.

### Polar term and orientation

Even equation (20) supplies only the Gamma factor up to scale and an irrelevant constant. It does not produce the polar factor `s(s-1)` of the completed zeta function. More importantly, a scalar determinant identity is not a positive quadratic-form theorem. The orientation problem of `WP-256` remains unchanged: the finite Weil autocorrelation has the wrong sign relative to the positive diagonal carrier.

Thus `WP-258` is not a claim that free-Fock geometry nearly proves RH. It closes one particularly canonical way of asking the branch's core local-to-global question: use the same `(H,N)`, the same arithmetic Gibbs weight, and zeta-regularize the gauge spectrum to obtain the archimedean completion.

## 8. Matched alphabet control

The mechanism is universal. Let a countable free alphabet have one-particle energies `epsilon_j>0` and partition function

\[
Q(\beta)=\sum_j e^{-\beta\epsilon_j}.
\tag{42}
\]

On the full free Fock space, the length-`m` Gibbs mass is

\[
Q(\beta)^m.
\tag{43}
\]

Therefore the weighted gauge zeta is

\[
\Phi(Q(\beta),u,z),
\tag{44}
\]

and it becomes Hurwitz exactly when

\[
Q(\beta)=1.
\tag{45}
\]

So the emergence of Gamma from the flattened length spectrum is a generic free-Fock phenomenon, not a Riemann-specific sign law. The rational-prime input determines the particular threshold `beta_*` through the prime zeta function. This matched control prevents treating equation (20) as arithmetic evidence beyond its exact source dictionary.

## 9. Prior art and novelty boundary

All special-function ingredients are classical. NIST DLMF §25.14 records the Lerch series and the specialization

\[
\Phi(1,u,z)=\zeta_H(u,z),
\]

while DLMF §25.11(vi), equation 25.11.18, records Lerch's formula

\[
\zeta_H'(0,z)=\log\Gamma(z)-\tfrac12\log(2\pi).
\]

The quasi-free Toeplitz--Cuntz/Pimsner equilibrium setting is also classical; Marcelo Laca and Sergey Neshveyev, *KMS states of quasi-free dynamics on Pimsner algebras*, J. Funct. Anal. 211 (2004), 457--482, DOI `10.1016/j.jfa.2003.08.008`, is the general prior-art anchor already relevant to `WP-256`--`WP-257`.

No novelty is claimed for Hurwitz zeta, Lerch transcendent, zeta determinants, Gamma regularization, free Fock space, or quasi-free KMS theory. The Mathia-specific durable content is the exact compatibility test between the two source-forced structures already present in the same prime Fock model:

\[
\boxed{
\text{WP-256 finite carrier at }c\beta=1
\quad\text{versus}\quad
\text{gauge-Hurwitz/Gamma determinant at }c\beta=\beta_*.
}
\tag{46}
\]

The two conditions cannot hold simultaneously.

## 10. Consequence for the Weil-positivity mandate

The free-prime Fock enlargement is more informative than a mere negative route. It now explains three different pieces of structure:

1. spectral multiplicity selects prime powers;
2. mean word energy and the one-particle boundary source the exact finite Mangoldt half-density;
3. the gauge number operator, after Gibbs weighting at the normalized Fock boundary, has a Hurwitz spectral zeta whose inverse determinant has the Gamma shape.

But these structures do **not** assemble at one intrinsic thermodynamic parameter. The finite coefficient and the archimedean Gamma factor are selected by different boundaries of the same source.

Accordingly, the next viable global mechanism cannot merely say "use the Fock gauge determinant for the real place." It must provide a source-derived reason why the finite sector is evaluated at the one-particle boundary while the archimedean sector is effectively radialized at a different Fock boundary, or replace this two-temperature picture by a genuinely global correspondence in which both arise from one operation. It must additionally derive the `pi` normalization, the polar sector, and the Weil orientation with an independent sign theorem.

`WP-258` therefore narrows, rather than resolves, the primary question: the same free-Fock geometry contains recognizable finite and archimedean ingredients, but its canonical Gibbs/gauge assembly does not make them compatible.