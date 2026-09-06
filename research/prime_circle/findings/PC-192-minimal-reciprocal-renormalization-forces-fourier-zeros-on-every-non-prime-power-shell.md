# PC-192 — minimal reciprocal renormalization forces Fourier zeros on every non-prime-power shell

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the minimally renormalized even reciprocal-amplitude family

\[
G_{n,\alpha}(x):=\Phi_n(e^{-|x|})^{-\alpha}-1,
\qquad \alpha>0.
\]

For every `n>1` that is **not** a prime power, the real Fourier transform of `G_{n,alpha}` has at least one nonzero real zero. In fact its high-frequency tail is forced to be negative,

\[
\widehat G_{n,\alpha}(t)
=-\frac{\alpha\varphi(n)}{t^2}+o(t^{-2}),
\qquad |t|\to\infty,
\]

while Fourier inversion and the exact endpoint identity `Phi_n(1)=1` force the total Fourier mass to vanish. Hence the transform must be positive somewhere before entering its negative tail and must cross zero. This closes the most immediate loophole left by PC-191: subtracting the asymptotic constant does restore real Fourier zeros, but it restores them on **every non-prime-power control shell**, including for non-integer reciprocal powers. Zero existence in this scalar completion is therefore anti-selective rather than a new RH mechanism.

This does **not** classify the zero locations or multiplicities, prime-power shells, signed combinations of different shells, matrix-valued/nonlocal kernels, cross-level assemblies, singular boundary operators, or global uniformization/monodromy.

## 1. The minimally renormalized even amplitude is intrinsic and integrable

Fix `n>1` and `alpha>0`. For `0<=r<=1`, `Phi_n(r)>0`: all roots of `Phi_n` lie on the unit circle, none lies on the positive interval `[0,1]`, and `Phi_n(0)=1`. Thus the real power below is unambiguous. Put

\[
g_{n,\alpha}(x)
:=\Phi_n(e^{-x})^{-\alpha}-1,
\qquad x\ge0,
\tag{1}
\]

and extend evenly,

\[
G_{n,\alpha}(x):=g_{n,\alpha}(|x|).
\tag{2}
\]

Because `Phi_n(z)=1+O(z)` as `z->0`, the function and all of its positive-half-line derivatives decay exponentially as `x->infinity`. In particular

\[
G_{n,\alpha}\in L^1(\mathbb R),
\qquad
g_{n,\alpha}''\in L^1(0,\infty).
\tag{3}
\]

The subtraction in (1) is the minimal scalar renormalization of the raw reciprocal amplitude: it removes its common value `1` at radial infinity and introduces no shell-dependent weight or spectral parameter.

The arithmetic endpoint is classical and exact:

\[
\Phi_n(1)=
\begin{cases}
p,&n=p^k,\\
1,&n>1\text{ is not a prime power}.
\end{cases}
\tag{4}
\]

Therefore every non-prime-power shell satisfies

\[
\boxed{G_{n,\alpha}(0)=0.}
\tag{5}
\]

That zero at the common-anchor endpoint will be the whole source of the Fourier sign constraint below.

## 2. Cyclotomic reciprocity fixes the cusp slope exactly

For every `n>1`, cyclotomic reciprocity gives

\[
\Phi_n(z)=z^{\phi}\Phi_n(z^{-1}),
\qquad \phi:=\varphi(n).
\tag{6}
\]

Differentiating (6) at `z=1` yields the standard self-reciprocal derivative identity

\[
2\Phi_n'(1)=\phi\Phi_n(1).
\tag{7}
\]

On a non-prime-power shell, (4) and (7) therefore give

\[
\Phi_n'(1)=\frac{\phi}{2}.
\tag{8}
\]

Differentiating (1), with `z=e^{-x}`, gives

\[
g_{n,\alpha}'(x)
=\alpha z\Phi_n'(z)\Phi_n(z)^{-\alpha-1}.
\tag{9}
\]

Consequently

\[
\boxed{
g_{n,\alpha}'(0+)
=\frac{\alpha\phi}{2}>0.
}
\tag{10}
\]

The even continuation (2) is continuous at the anchor but has the exact derivative jump

\[
G_{n,\alpha}'(0+)-G_{n,\alpha}'(0-)
=\alpha\phi.
\tag{11}
\]

Thus the minimal renormalization replaces the smooth positive-product completion of PC-191 by a cusp whose strength is completely fixed by the shell cardinality `varphi(n)`. No zeta datum has entered.

## 3. The cusp forces a universal negative `t^{-2}` Fourier tail

Use the Fourier convention

\[
\widehat G_{n,\alpha}(t)
:=\int_{\mathbb R}G_{n,\alpha}(x)e^{-itx}\,dx
=2\int_0^\infty g_{n,\alpha}(x)\cos(tx)\,dx.
\tag{12}
\]

For `t!=0`, two integrations by parts on the half-line give

\[
\int_0^\infty g_{n,\alpha}(x)\cos(tx)\,dx
=-\frac{g_{n,\alpha}'(0+)}{t^2}
-\frac1{t^2}
\int_0^\infty g_{n,\alpha}''(x)\cos(tx)\,dx.
\tag{13}
\]

The second derivative is integrable by (3), so the Riemann--Lebesgue lemma makes the last integral `o(1)`. Inserting (10) therefore yields the exact leading asymptotic

\[
\boxed{
\widehat G_{n,\alpha}(t)
=-\frac{\alpha\varphi(n)}{t^2}+o(t^{-2})
\qquad (|t|\to\infty).
}
\tag{14}
\]

In particular there exists `T<infinity` such that

\[
\widehat G_{n,\alpha}(t)<0
\qquad (|t|>T).
\tag{15}
\]

Equation (14) also implies `widehat G in L^1(R)`. The endpoint expansion itself is standard Fourier analysis: repeated integration by parts for half-line Fourier integrals gives exactly this boundary-jet asymptotic. NIST DLMF §2.3(i), especially Eq. 2.3.5, records the general classical expansion. The Prime-Circle content is the cyclotomic specialization (10), not a new Fourier-asymptotics theorem.

## 4. Exact zero Fourier mass forces a positive lobe and hence a real zero

We now use the part of the argument that does not follow from the negative tail alone. Since both `G` and `widehat G` are integrable, Fourier inversion at the continuous point `x=0` gives

\[
G_{n,\alpha}(0)
=\frac1{2\pi}\int_{\mathbb R}\widehat G_{n,\alpha}(t)\,dt.
\tag{16}
\]

For a non-prime-power shell, (5) makes the left side zero. Hence

\[
\boxed{
\int_{\mathbb R}\widehat G_{n,\alpha}(t)\,dt=0.
}
\tag{17}
\]

But (15) says that the transform is strictly negative on both sufficiently large tails. Therefore it cannot be nonpositive everywhere: otherwise its integral would be strictly negative. There must exist some real `t_+` with

\[
\widehat G_{n,\alpha}(t_+)>0.
\tag{18}
\]

The Fourier transform is continuous and even. Moving from the positive point (18) toward the eventually negative region (15), the intermediate-value theorem gives a positive real zero `tau>0`. Evenness gives its partner at `-tau`. Thus

\[
\boxed{
\forall n>1\text{ non-prime-power},\ \forall\alpha>0,
\quad
\exists\tau>0:\
\widehat G_{n,\alpha}(\pm\tau)=0.
}
\tag{19}
\]

No assumption on RH, prime distribution, or a limiting conductor is used.

## 5. The mixed-prime control is not exceptional; it is the entire non-prime-power class

The smallest mixed-prime control is `n=6`, where

\[
\Phi_6(r)=1-r+r^2
\]

and for `alpha=1`

\[
G_{6,1}(x)
=\frac{e^{-|x|}(1-e^{-|x|})}
{1-e^{-|x|}+e^{-2|x|}}.
\tag{20}
\]

This function is positive away from the anchor, so its transform is positive at `t=0`; (14) makes it negative at high frequency, already forcing a zero by continuity. Equation (19) is stronger: positivity of the physical-space profile or of the zero-frequency Fourier mode is unnecessary. It applies equally to levels such as `10,12,15,18,20,21,30,...`, including cases where the radial profile changes sign or the transform at zero is not positive.

The decisive matched-control statement is therefore not merely that *some* composite conductor can mimic a Fourier zero. It is

\[
\boxed{
\Phi_n(1)=1
\quad\Longrightarrow\quad
\text{the minimally renormalized even reciprocal amplitude has a nonzero real Fourier zero.}
}
\tag{21}
\]

For `n>1`, the antecedent is exactly the classical condition that `n` is not a prime power.

## 6. Prior-art and novelty audit

All general ingredients are classical. Cyclotomic self-reciprocity and the value of `Phi_n(1)` are standard cyclotomic identities already used elsewhere in this line. The `t^{-2}` tail is the ordinary endpoint expansion of a Fourier integral obtained by repeated integration by parts; DLMF §2.3(i) records the general half-line formula. Fourier inversion then converts the exact endpoint value into the zero-total-mass constraint (17).

Directed searches for Fourier transforms of reciprocal cyclotomic amplitudes, `Phi_n(e^{-x})`, rational-exponential quotients such as the `n=2p` controls, and cyclotomic Fourier-zero criteria did not locate a source packaging (19) as an arithmetic or RH theorem. That absence is **not** treated as a novelty claim. The durable result is a Prime-Circle boundary obtained by combining standard facts: the most immediate renormalized scalar repair of PC-191 necessarily manufactures Fourier zeros throughout the non-prime-power control class.

This also explains why the result is not evidence toward RH. The zeros are forced by two local/analytic facts only: the common-anchor endpoint vanishes after subtraction, and the even continuation has a derivative cusp. Their existence does not encode the Riemann zero ordinates, a functional equation in a complex spectral parameter, or a critical line.

## 7. What this rules out and what remains open

PC-191 proved that the unique inversion-even half-growth completion of the **raw** integer reciprocal amplitude has a strictly positive real Fourier transform, while explicitly leaving the minimally renormalized difference and non-integer powers open. PC-192 closes the zero-existence version of both loopholes simultaneously for

\[
\Phi_n(e^{-|x|})^{-\alpha}-1,
\qquad \alpha>0:
\]

if the shell is not a prime power, real Fourier zeros are unavoidable for elementary endpoint reasons. Thus the route

\[
\text{minimal reciprocal renormalization}
\longrightarrow
\text{real Fourier zeros}
\longrightarrow
\text{prime/RH spectral mechanism}
\]

fails before any comparison with the Riemann zero set.

The theorem deliberately does not say that prime-power shells are zero-free, nor does it classify where the zeros in (19) lie. A future candidate could still use a quantitatively rigid zero-location law, a signed combination whose coefficients are forced by cross-shell geometry, a matrix-valued/nonlocal operator, an all-shell limit, or global uniformization. Such a candidate must survive matched non-prime-power controls rather than treating the mere appearance of Fourier zeros as evidence.

## 8. Audit checks

The claim is exact and has short independent falsifiers:

- verify `Phi_n(1)=1` for a non-prime-power control and `2 Phi_n'(1)=varphi(n) Phi_n(1)` from reciprocity;
- differentiate (1) and recover the right slope `alpha varphi(n)/2`;
- integrate (12) twice by parts and check the sign and factor in `-alpha varphi(n)/t^2`;
- verify that `g''` is integrable, so the Riemann--Lebesgue remainder is `o(t^-2)` and `widehat G` is integrable;
- apply Fourier inversion at the exact endpoint `G(0)=0`; a transform that stayed nonpositive after its negative tail would contradict zero total Fourier mass;
- any non-prime-power `n>1` and `alpha>0` for which `widehat G` has no nonzero real zero would falsify (19).

## Research consequence

The scalar inversion branch now has a sharp dichotomy. Keeping the raw reciprocal amplitude in the intrinsic half-growth gauge gives the strictly positive strip-Poisson spectrum of PC-191. Removing the asymptotic constant before the even extension creates a common-anchor cusp; on every non-prime-power shell that cusp and the exact endpoint value force real Fourier zeros. **Neither side supplies an RH mechanism:** one side has no real zeros, while the other manufactures them throughout the matched control class.

Any surviving Fourier/spectral route must therefore extract more than zero existence from a single renormalized shell. It must introduce a source-forced relation among zero locations, cross-shell data, or genuinely nonlocal/global structure that cannot be reduced to the endpoint/cusp mechanism above.