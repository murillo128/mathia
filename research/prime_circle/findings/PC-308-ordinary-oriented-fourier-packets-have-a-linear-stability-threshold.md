# PC-308 — ordinary oriented Fourier packets have a linear stability threshold

**Status:** `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the larger-bandwidth escape left open by PC-307.

PC-306 proves that the canonical prime source and its one-step translate are disjoint while their first `K=o(q)` additive Fourier modes converge together, and PC-307 strengthens the required amplification throughout every fixed polylogarithmic bandwidth. The remaining obvious escape was to increase the number of *ordinary, unweighted* oriented Fourier coordinates much further.

For that specific carrier there is an exact scale transition. Sublinear bandwidth can never retain a fixed separation, while linear bandwidth already can. The first robust witnesses are not a new zeta-sensitive channel: they are classical fixed-denominator major-arc/congruence resonances of the primes. In particular, the parity resonance at mode `(q-1)/2` gives the explicit limit

\[
\boxed{
\left|F_q^+\!\left(\frac{q-1}{2}\right)
      -F_q\!\left(\frac{q-1}{2}\right)\right|
\longrightarrow \frac4\pi .
}
\tag{1}
\]

Thus merely expanding an ordinary oriented packet eventually repairs the topological instability of PC-306, but only when the packet reaches `Theta(q)` frequencies, at which point it is already resolving fixed congruence structure of the input source. This closes “larger ordinary Fourier bandwidth” as an unexplained intermediate RH carrier.

## 1. Matched source and packet distance

Let `q>3` be prime and

\[
P_q:=\{p:2<p<q,\ p\text{ prime}\},
\qquad
M_q:=|P_q|=\pi(q)-2.
\tag{2}
\]

Write the normalized additive Fourier coefficients

\[
F_q(k):=\frac1{M_q}\sum_{p\in P_q}e\!\left(\frac{kp}{q}\right),
\qquad e(x):=e^{2\pi i x}.
\tag{3}
\]

For the one-step translated support `P_q^+=P_q+1`,

\[
F_q^+(k)=e(k/q)F_q(k),
\tag{4}
\]

and `P_q` and `P_q^+` are disjoint because the former contains only odd primes and the latter only even residues. Hence their source measures stay at total-variation distance one.

For a positive-frequency packet define

\[
\Delta_q(K)
:=
\max_{1\le k\le K}|F_q^+(k)-F_q(k)|.
\tag{5}
\]

PC-306 gives, for `K\le q/2`,

\[
\Delta_q(K)
\le 2\pi\frac Kq.
\tag{6}
\]

Therefore

\[
\boxed{
K_q=o(q)
\quad\Longrightarrow\quad
\Delta_q(K_q)\to0.
}
\tag{7}
\]

This already rules out **every** sublinear ordinary bandwidth, not only the polylogarithmic regime sharpened in PC-307. No arithmetic estimate enters (7); it is forced by the exact translation phase.

## 2. The parity mode gives fixed separation at linear bandwidth

Take

\[
k_q:=\frac{q-1}{2}.
\tag{8}
\]

Every `p\in P_q` is odd, so

\[
\begin{aligned}
e\!\left(\frac{k_qp}{q}\right)
&=
\exp\!\left(\pi i p\left(1-\frac1q\right)\right)\\
&=-e^{-\pi i p/q}.
\end{aligned}
\tag{9}
\]

Consequently

\[
F_q(k_q)
=-\frac1{M_q}\sum_{p\in P_q}e^{-\pi i p/q}.
\tag{10}
\]

The ordinary prime number theorem, by Stieltjes partial summation, implies weak convergence of the scaled prime empirical measure to Lebesgue measure on `[0,1]`: for every continuously differentiable `f`,

\[
\frac1{M_q}\sum_{p\in P_q}f(p/q)
\longrightarrow
\int_0^1 f(t)\,dt.
\tag{11}
\]

Applying (11) to `f(t)=e^{-\pi i t}` gives

\[
\boxed{
F_q(k_q)
\longrightarrow
-\int_0^1e^{-\pi i t}\,dt
=rac{2i}{\pi}.
}
\tag{12}
\]

At the same time,

\[
e(k_q/q)-1
\longrightarrow e(1/2)-1=-2.
\tag{13}
\]

Using (4),

\[
F_q^+(k_q)-F_q(k_q)
=(e(k_q/q)-1)F_q(k_q)
\longrightarrow
-\frac{4i}{\pi},
\tag{14}
\]

which proves (1). Hence

\[
\boxed{
\liminf_{q\to\infty}\Delta_q((q-1)/2)
=\frac4\pi>0.
}
\tag{15}
\]

Together, (7) and (15) locate the stable-separation transition at the **linear frequency scale**: `o(q)` modes cannot give a fixed margin for this matched pair, whereas `Theta(q)` modes already can.

The mechanism in (9) is completely transparent. The near-Nyquist Fourier phase converts the oddness of every prime in `P_q` into a coherent sign before the slowly varying envelope `e^{-\pi i p/q}` is averaged. The stable signal is parity plus the smooth PNT density, not a fluctuation coming from zeta zeros.

## 3. Every positive linear fraction contains a classical rational resonance

The parity witness is the simplest member of a fixed-denominator family. Fix a squarefree integer `m>=2`. For every sufficiently large prime `q` with `q\nmid m`, let `r_q\in\{1,\ldots,m-1\}` be the residue of `q` modulo `m` and put

\[
k_{q,m}:=\frac{q-r_q}{m}.
\tag{16}
\]

Then `k_{q,m}/q\to1/m`. Grouping the sum (3) by prime residue classes modulo `m` and using the prime number theorem in the fixed arithmetic progressions `a mod m` gives

\[
F_q(k_{q,m})
=
\frac{\mu(m)}{\varphi(m)}
\int_0^1 e\!\left(-\frac{r_qt}{m}\right)dt
+o_m(1).
\tag{17}
\]

The finite residue factor is exactly the Ramanujan sum

\[
\sum_{a\in(\mathbb Z/m\mathbb Z)^\times}e(a/m)
=c_m(1)=\mu(m).
\tag{18}
\]

Since `m` is squarefree, `|\mu(m)|=1`, and since `1\le r_q<m`, the integral in (17) never vanishes. Thus

\[
\left|F_q^+(k_{q,m})-F_q(k_{q,m})\right|
\to
\frac{2\sin(\pi/m)}{\varphi(m)}
\frac{m\sin(\pi r_q/m)}{\pi r_q}
\tag{19}
\]

along each residue class of `q mod m`; the finitely many possible right-hand sides are all strictly positive.

This gives a useful sharp form of the scale statement. If a bandwidth sequence satisfies

\[
\liminf_{q\to\infty}\frac{K_q}{q}>0,
\tag{20}
\]

choose a fixed squarefree `m` with `1/m` smaller than that lower limit. Then `k_{q,m}\le K_q` for all sufficiently large `q`, and (19) yields

\[
\boxed{
\liminf_{q\to\infty}\Delta_q(K_q)>0.
}
\tag{21}
\]

So for ordinary unweighted Fourier packets the matched translation control has a genuine dichotomy in scale:

\[
K_q=o(q)\Rightarrow\text{no fixed margin},
\qquad
K_q\ge c q\Rightarrow\text{a fixed margin is available}.
\tag{22}
\]

What appears at the linear scale is precisely the fixed-denominator major-arc structure of the primes.

## 4. Prior-art and novelty audit

No new analytic-number-theory theorem is being claimed. Equation (11) is an immediate consequence of the prime number theorem. Equation (17) is the equally classical fixed-modulus prime number theorem in arithmetic progressions plus partial summation. The factor (18) is the standard Ramanujan sum. In the Hardy--Littlewood circle method, large prime exponential sums near rationals with small denominator are exactly the classical **major arcs**; the residue-class main term is encoded by finite Ramanujan sums. Vaughan's *The Hardy--Littlewood Method* and Montgomery--Vaughan's classical multiplicative-number-theory treatment are standard references for this framework. A targeted literature audit found the same classification: modern work on exponential sums over primes still treats large values as rational/major-arc behavior, not as a new roots-of-unity spectral mechanism.

Accordingly, the novelty claim is only project-local. PC-307 left substantially larger bandwidth as a legitimate escape from its polylogarithmic conditioning bound. Equations (7)--(22) classify the ordinary unweighted version of that escape: **stable separation begins only at linear bandwidth, and the stable modes are already classical congruence major arcs.** No new `SOURCES.md` dependency is introduced because the load-bearing inputs are the same standard PNT/PNT-in-progressions and Ramanujan-sum machinery already used and classicalized throughout this line.

This also passes the matched-control audit in the intended direction. The control is not a synthetic random source: it is the exact one-vertex rotation of the canonical source, disjoint from it for every `q>3`. The fact that linear modes separate the pair therefore does not certify a prime-specific RH mechanism; the explicit witness shows why the separation occurs and why parity/congruence information suffices.

## 5. Boundary for the research line

PC-306 showed that exact finite-level source information can be algebraically present while analytically unstable. PC-307 then showed that adding any fixed-power polylogarithmic number of ordinary Fourier coordinates still requires nearly `q log q` conditioning for a fixed-margin discriminator. The present result closes the remaining ordinary-bandwidth interpolation:

- no `o(q)` packet can stably separate the canonical source from its one-step translate in packet sup norm;
- a positive linear fraction of the Fourier spectrum can stably separate them;
- the first explicit stable family is fixed-denominator parity/congruence data, classicalized by PNT in arithmetic progressions and Ramanujan major arcs.

Therefore **increasing ordinary Fourier bandwidth is not a hidden intermediate bridge to RH**. Below linear scale it remains topologically unstable; at linear scale it starts reading elementary congruence structure and is already on the way to the complete source reconstruction classified in PC-304.

The conclusion does not cover singular mode weights, a different geometry-forced topology, exact `Li` subtraction followed by controlled amplification, or an operator coupling different conductors *before* an ordinary packet is formed. Those are still admissible only if their amplification/topology is intrinsic and their output survives the same matched-source and prior-art tests. In particular, an RH-sensitive candidate must contribute more than the classical major-arc information isolated here.

## 6. Falsification and finite controls

The parity identity is directly testable without asymptotics. For each odd prime `q`, compute `F_q((q-1)/2)` from (3) and verify the exact rewrite (10). The two normalized quantities must satisfy

\[
F_q((q-1)/2)\to 2i/\pi,
\qquad
F_q^+((q-1)/2)-F_q((q-1)/2)\to-4i/\pi.
\tag{23}
\]

For a fixed squarefree `m`, group primes by residue modulo `m` and compare the mode `k_{q,m}` with (17). Failure of the finite residue factor to equal `c_m(1)=\mu(m)`, or a vanishing limit in a reduced residue class `r_q`, would falsify the rational-resonance derivation.

Finally, any sequence `K_q=o(q)` for which the unweighted packet distance (5) stays bounded below by a positive constant would contradict the exact bound (6), independently of all prime-distribution input.