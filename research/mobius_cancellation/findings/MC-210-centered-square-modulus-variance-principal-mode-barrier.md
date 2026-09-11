# MC-210 — Centered square-modulus variance leaves a Mertens-complete principal mode

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-209` replaces the absolute large-square-divisor tail by the dyadic prescribed-residue energy

\[
V_D=\sum_{\substack{D<d\le 2D\\(d,q)=1\\d^2\le X}}d\,|A_d(T)|^2,
\qquad
A_d(T)=\sum_{\substack{n\le T\\(n,q)=1\\n\equiv-q\pmod{d^2}}}\mu(n),
\tag{1}
\]

where

\[
q=\prod_{p\le y}p,\qquad y=c\log X,\qquad T=X-q.
\tag{2}
\]

The target `V_D\ll X^{1+o(1)}` was described there as a Barban--Davenport--Halberstam / averaged-Chowla type variance problem. There is a load-bearing qualification: **the target in `(1)` is uncentered and uses one source-prescribed residue. Standard centered progression variance removes a principal mode which, in the present logarithmic primorial regime, is fixed-power equivalent to a Mertens prefix under a subpower-cost exact transform.**

Because the linear shell

\[
\Delta_D=-\sum_d\mu(d)A_d(T)
\tag{3}
\]

only sees square-free `d`, the sufficient energy can first be sharpened to

\[
\boxed{
W_D:=\sum_{\substack{D<d\le2D\\(d,q)=1\\d^2\le X}}
 d\,\mu^2(d)|A_d(T)|^2.
}
\tag{4}
\]

Indeed

\[
\boxed{
|\Delta_D|^2
\le
\left(\sum_{D<d\le2D}\frac{\mu^2(d)}d\right)W_D
\ll W_D.
}
\tag{5}
\]

Thus `W_D\ll X^{1+o(1)}` on the required shells is already enough for the `MC-209` implication, and non-square-free root moduli need not be controlled at all.

Now fix a square-free `d` occurring in `(4)` and, for every reduced residue `a (mod d^2)`, put

\[
A_{d,a}(T)
:=
\sum_{\substack{n\le T\\(n,q)=1\\n\equiv a\pmod{d^2}}}\mu(n).
\tag{6}
\]

Since `(a,d)=1`, every integer counted in `(6)` is automatically coprime to `d`. Hence

\[
\boxed{
\sum_{a\,({\rm mod}\ d^2)}^{*}A_{d,a}(T)
=R_{qd}(T),
}
\qquad
R_Q(U):=\sum_{\substack{n\le U\\(n,Q)=1}}\mu(n).
\tag{7}
\]

Therefore the exact reduced-residue mean is

\[
\boxed{
m_d(T)=\frac{R_{qd}(T)}{\varphi(d^2)},
}
\tag{8}
\]

and the prescribed residue from `MC-209` decomposes as

\[
\boxed{
A_d(T)=m_d(T)+E_{d,-q}(T),
\qquad
\sum_a^*E_{d,a}(T)=0.
}
\tag{9}
\]

The centered term `E` is the natural object controlled by ordinary BDH-type variance; the mean `(8)` is projected out.

For the moving moduli `Q=qd` in this branch, that projected mode is not a cheap density term. Let

\[
\mathcal S_Q:=\{r\ge1: p\mid r\Rightarrow p\mid Q\}.
\tag{10}
\]

Then the coefficient identity already underlying the logarithmic rough split extends exactly to `Q=qd`:

\[
\boxed{
\mu(n)\mathbf 1_{(n,Q)=1}
=(\mu*\mathbf 1_{\mathcal S_Q})(n).
}
\tag{11}
\]

Because `q` and `d` are square-free and coprime, the convolution inverse is also finite and exact:

\[
\boxed{
\mu
=
\bigl(\mu\mathbf 1_{(\cdot,Q)=1}\bigr)
*
\bigl(\mu\mathbf 1_{\{e:e\mid Q\}}\bigr).
}
\tag{12}
\]

Summing `(11)`--`(12)` gives the two prefix transforms

\[
\boxed{
R_Q(U)=\sum_{\substack{r\le U\\r\in\mathcal S_Q}}M(U/r),
}
\tag{13}
\]

and

\[
\boxed{
M(U)=\sum_{\substack{e\mid Q\\e\le U}}\mu(e)R_Q(U/e).
}
\tag{14}
\]

At `y=c\log X` and uniformly for square-free `d\le\sqrt X` with `(d,q)=1`, both transform kernels have only subpower complexity:

\[
\boxed{
\tau(qd)=X^{o(1)},
\qquad
|\mathcal S_{qd}\cap[1,X]|=X^{o(1)}.
}
\tag{15}
\]

Consequently, on prefix families stable under the dilations appearing in `(13)`--`(14)`, any fixed-power estimate

\[
M(U)\ll X^{o(1)}U^\theta
\tag{16}
\]

transfers to `R_{qd}(U)` with the same exponent, and conversely a uniform estimate of that form for `R_{qd}` transfers back to `M`. The principal residue mean `(8)` is therefore a **Mertens-complete mode at fixed-power resolution**, not merely an elementary main term that a centered progression theorem may discard harmlessly.

This yields a precise boundary for the `MC-209` variance route. If one attempts to prove `(4)` by splitting the prescribed residue into mean plus centered fluctuation and controlling the two pieces separately, define

\[
P_D:=\sum_d d\mu^2(d)\frac{|R_{qd}(T)|^2}{\varphi(d^2)^2},
\qquad
Z_D:=\sum_d d\mu^2(d)|E_{d,-q}(T)|^2.
\tag{17}
\]

Then

\[
W_D\le2P_D+2Z_D.
\tag{18}
\]

Because every prime factor of `d` exceeds `y=c\log X`, uniformly for `d\le\sqrt X`,

\[
\varphi(d^2)=d^2\bigl(1+o(1)\bigr).
\tag{19}
\]

Thus a hypothetical separate principal-prefix estimate

\[
|R_{qd}(T)|\le X^{\theta+o(1)}
\tag{20}
\]

uniformly on a shell gives only

\[
\boxed{
P_D\ll \frac{X^{2\theta+o(1)}}{D^2}.
}
\tag{21}
\]

To make `(21)` diagonal-scale, `P_D\ll X^{1+o(1)}`, one needs

\[
\boxed{
D\ge X^{\theta-1/2-o(1)}.
}
\tag{22}
\]

At the lowest root-modulus shells `D=X^{o(1)}` this separate strategy therefore requires `theta\le1/2+o(1)`: essentially the critical Mertens exponent for the principal mode. A fixed-power improvement `theta<1` would only move the threshold to `D\ge X^{\theta-1/2+o(1)}`; it would not cover all shells unless it reaches the critical exponent.

The conclusion is not that `(4)` is Mertens-equivalent, nor that the variance route fails. It is more specific: **a proof which imports a standard centered BDH theorem for the transverse residue fluctuations and then estimates the removed mean independently has reintroduced the original Mertens-scale problem in the low square-modulus shells.** A successful variance proof must instead obtain the raw prescribed-residue energy directly, exploit cancellation/interference between principal and transverse pieces that is destroyed by `(18)`, or supply genuinely new arithmetic control of the principal mode.

No estimate `W_D\ll X^{1+o(1)}`, no improved bound for `M(X)`, and no zero-free or RH consequence is proved here.

## 1. The square-free energy is the exact Cauchy target

Equation `(5)` is simply weighted Cauchy--Schwarz applied to `(3)`:

\[
\left|\sum_d\mu(d)A_d\right|^2
\le
\left(\sum_d\frac{\mu^2(d)}d\right)
\left(\sum_d d\mu^2(d)|A_d|^2\right).
\]

On `D<d\le2D`, the first factor is at most `\sum 1/d\ll1`. This removes from `MC-209` every root modulus that the original linear transform already kills through `mu(d)=0`. It yields only a logarithmic/density-level structural improvement, not a new fixed-power estimate.

The retained moduli are square-free and `y`-rough. That extra structure may be analytically useful later, but the present finding makes no large-sieve or dispersion claim from it.

## 2. Centering projects out exactly the rough principal prefix

For reduced `a (mod d^2)`, the congruence condition forces `(n,d)=1`. Therefore summing `(6)` over all reduced residues counts each `n\le T` with `(n,qd)=1` exactly once, proving `(7)`--`(9)` without characters.

Equivalently, Dirichlet-character orthogonality gives

\[
A_{d,a}(T)
=
\frac1{\varphi(d^2)}
\sum_{\chi\,({\rm mod}\ d^2)}
\overline{\chi(a)}
\sum_{\substack{n\le T\\(n,q)=1}}\mu(n)\chi(n),
\tag{23}
\]

and the principal character contributes exactly `(8)`. Centered variance discards that character.

This is the square-modulus specialization of the zero-mode/transverse distinction already exposed for the primorial residue vector in `MC-188`, but the consequence is new for the live `MC-209` theorem surface: the raw prescribed-residue energy cannot be replaced silently by a standard centered variance.

## 3. The moving `qd` principal mode is subpower-reversible

The local Euler-factor proof of `(11)` is exact. At a prime `p\mid Q`, the local factors of `mu` and `1_{S_Q}` are `(1-z)` and `(1-z)^{-1}`, so they cancel to `1`; at `p\nmid Q`, the second factor is `1`, leaving `(1-z)`. The inverse `(12)` follows by multiplying at each `p\mid Q` by `(1-z)` again.

It remains to justify the uniform subpower complexity in `(15)`. Since

\[
\pi(y)=O\!\left(\frac{\log X}{\log\log X}\right),
\qquad
\omega(d)\le\frac{\log d}{\log y}
=O\!\left(\frac{\log X}{\log\log X}\right),
\]

one immediately has

\[
\tau(qd)=2^{\pi(y)+\omega(d)}=X^{o(1)}.
\tag{24}
\]

For the semigroup count, factor every `r\in S_{qd}` uniquely as `r=ab`, where `a` is `y`-smooth and every prime factor of `b` divides `d`. The logarithmic-smooth count `Psi(X,y)=X^{o(1)}` was established in `MC-181` by Rankin's method. If `k=\omega(d)` and `L=\lfloor\log X/\log y\rfloor`, then a number `b\le X` supported on the primes of `d` has total exponent at most `L`; hence the number of possible exponent vectors is at most

\[
\binom{k+L}{L}\le2^{k+L}=X^{o(1)}.
\tag{25}
\]

Multiplying the two subpower counts proves the second statement in `(15)`.

Now `(13)`--`(14)` and the triangle inequality prove the fixed-power transfer in both directions. The qualifier **prefix family stable under dilation** is essential. A bound for the single terminal value `R_{qd}(T)` does not control the values `R_{qd}(T/e)` required by `(14)` and is not asserted to imply a Mertens bound by itself.

## 4. The low-shell phase boundary for separate principal control

For `(19)`, since every prime `p\mid d` satisfies `p>y`,

\[
\sum_{p\mid d}\frac1p
\le
\frac{\omega(d)}y
\le
\frac{\log d}{y\log y}
=O\!\left(\frac1{\log\log X}\right).
\tag{26}
\]

Therefore

\[
\frac{\varphi(d)}d
=\prod_{p\mid d}(1-1/p)
=1+O(1/\log\log X),
\]

which proves `(19)`. Inserting `(20)` into `(17)` then gives

\[
P_D
\ll
X^{2\theta+o(1)}
\sum_{D<d\le2D}\frac1{d^3}
\ll
\frac{X^{2\theta+o(1)}}{D^2},
\]

proving `(21)`--`(22)`.

This exponent calculation deliberately assumes a pointwise/uniform principal estimate in order to diagnose the common centered-plus-mean strategy. It is **not** a lower bound for `P_D`: cancellation or averaging across the family `R_{qd}` may conceivably prove `P_D\ll X` by a different mechanism even when no individual critical bound is known. Such a theorem would itself be new signed arithmetic information and would be a legitimate escape.

## 5. Prior-art audit

The algebraic rough/smooth transform is classical and is already internalized in `MC-181`, which proves subpower reversibility of the logarithmic rough split for local variance. `MC-187` uses the same forward convolution to transfer classical Mertens cancellation to the logarithmically rough zero mode. No novelty is claimed for `(11)`--`(15)` as abstract convolution identities.

`MC-188` already establishes the conceptual warning at the primorial modulus: the smooth-modulus dispersion theorem of Klurman--Mangerel--Teräväinen controls transverse residue fluctuations while projecting out the rough Möbius zero mode. The present result transports that warning to the **square-modulus prescribed-residue energy introduced only in `MC-209`**, where the extra modulus `d^2` changes the mean to `R_{qd}/phi(d^2)` and produces the quantitative shell threshold `(22)`.

Adam J. Harper, *Simple Barban--Davenport--Halberstam type asymptotics for general sequences*, Journal of the London Mathematical Society 112 (2025), e70293, DOI `10.1112/jlms.70293`, defines the general-sequence BDH variance by subtracting, for each modulus and gcd class, the average of the sequence over that class before squaring and summing over residues. For the reduced classes modulo `d^2` in `(6)`, that standard centering is exactly `(8)`--`(9)`. Harper's theorem is therefore adjacent prior art for the transverse object, not a black-box estimate for the raw one-residue energy `(4)`.

The durable mathematical delta is the combined line-specific reduction: **the `MC-209` variance target has two conceptually different proof interfaces.** A centered-BDH interface exposes a principal `R_{qd}` mode whose low-shell separate control reaches the Mertens critical exponent, while a raw prescribed-residue interface is allowed to exploit arithmetic interference that centering destroys. Future applications of progression-variance prior art must state which interface they actually control.

## 6. Boundaries and falsification tests

- The result does not show that `W_D`, `V_D`, or the square-defect transform is equivalent to RH. The prescribed residue may exhibit cancellation between principal and nonprincipal character components that is invisible after separate absolute estimates.
- Equation `(18)` is only a sufficient decomposition. Failure to bound `P_D` and `Z_D` separately does not falsify the raw variance route.
- The fixed-power equivalence `(13)`--`(16)` requires prefix-uniform control over the dilation family generated by `qd`; a terminal-point estimate alone is not Mertens-complete.
- The subpower count `(15)` uses `y=c log X`, square-free `d`, `(d,q)=1`, and `d<=sqrt X`. It is not asserted for polynomial sifting levels or unrestricted extra prime sets.
- The threshold `(22)` diagnoses uniform pointwise principal control. A genuinely averaged theorem for the family `R_{qd}` could beat that bookkeeping and would constitute new arithmetic input rather than a consequence of centered BDH.
- `W_D` is a strictly more faithful sufficient energy than `V_D` because it retains only root moduli present in the original linear sum, but no fixed-power saving follows from this support restriction alone.
- A future claim that an all-residue centered variance theorem proves the `MC-209` target must explicitly restore `(8)` or exhibit a coupled argument that controls the prescribed residue without separating its principal and transverse components.