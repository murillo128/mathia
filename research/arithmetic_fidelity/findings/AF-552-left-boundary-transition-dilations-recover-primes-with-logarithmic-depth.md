# AF-552 — Left-boundary transition dilations recover primes with logarithmic depth

## Status

EXACT-DERIVED · LITERATURE+DERIVED · ARITHMETIC-FIDELITY · DIRICHLET-TAIL · BOUNDARY-DILATION · CONDITIONING · MATCHED-CONTROL · NO-NOVELTY-CLAIM

## Claim

AF-550 proves that the complete prime-tail transitions
[
H_n=P^{-1}circ T_n,
qquad
P(s)=sum_p p^{-s},
qquad
T_n(s)=sum_{kge n}p_k^{-s},
]
exactly quotient arbitrary common monotone recalibration of the tail values. AF-551 then shows that the absolute prime scale is exponentially ill-conditioned when it is read from the right-tail residual as (s	oinfty).

The same invariant profiles contain a different, source-natural carrier at the common divergence boundary (s=1). Extend (H_n) continuously by (H_n(1)=1). Then the one-sided boundary derivative exists and is
[
oxed{
D_n:=H_n'(1+)
=
exp!left(sum_{k<n}rac1{p_k}ight).
}
	ag{1}
]
Consequently adjacent boundary dilations recover every rational prime exactly:
[
oxed{
log D_{n+1}-log D_n=rac1{p_n},
qquad
p_n=rac1{log D_{n+1}-log D_n}.
}
	ag{2}
]
No external anchor such as (p_1=2) is needed: (D_1=1) and (D_2=e^{1/2}) already recover the first prime.

This boundary carrier also has a substantially milder source-depth law than AF-551's right-tail residual. Let
[
x_n>0,qquad x_nlog p_nlongrightarrow0,
]
and write
[
y_n(x)=H_n(1+x)-1,
qquad
L_n(x)=lograc{y_{n+1}(x)}{y_n(x)}.
]
Then
[
oxed{
p_n L_n(x_n)longrightarrow1.
}
	ag{3}
]
Thus finite samples need approach the common boundary only at the reciprocal-logarithmic scale
[
s_n-1=o!left(rac1{log p_n}ight)
]
to retain the reciprocal-prime signal asymptotically. This does not make the inverse problem uniformly noise-stable: the signal itself is (1/p_n), so observation error in (L_n) must shrink with the prime scale.

The finite-prefix generalized-prime control used by AF-551 confirms that this is genuinely a different information channel. For
[
q_1=2^c,quad q_2=3^c,quad q_3=5^c,quad q_k=p_k (kge4),
qquad
1<c<rac{log7}{log5},
]
the right-tail quotient profiles become exponentially close in AF-551's moving-tail horizontal metric, but the left-boundary dilation already separates the systems by
[
H_2'(1+)=e^{1/2},
qquad
K_2'(1+)=e^{2^{-c}}.
	ag{4}
]
For fixed (c
e1) this is a fixed nonzero gap. AF-551's exponential conditioning lower bound is therefore a theorem about its right-tail absolute-scale channel, not an intrinsic conditioning law for the entire full-profile quotient.

## Prime-zeta boundary normal form

The classical Möbius-inversion representation of the prime zeta function gives, in a real neighborhood to the right of (s=1),
[
P(1+x)=-log x+C_0+R(x),
qquad x>0,
	ag{5}
]
where (R) extends analytically across (x=0). The singular coefficient is exactly one. The constant (C_0) is irrelevant below because it cancels from every transition identity.

For fixed (n), define the deleted prefix
[
A_n(s)=sum_{k<n}p_k^{-s},
]
so that
[
T_n(s)=P(s)-A_n(s).
	ag{6}
]
Set
[
y_n(x)=H_n(1+x)-1.
]
The transition identity (P(H_n(1+x))=T_n(1+x)), together with (5)--(6), gives the exact equation
[
oxed{
lograc{y_n(x)}x
=
A_n(1+x)+R(y_n(x))-R(x).
}
	ag{7}
]

Equation (7), rather than a separate asymptotic ansatz, is the boundary normal form for the transition.

## Exact recovery from boundary dilations

Let
[
a_n=sum_{k<n}rac1{p_k}.
]
For fixed (n), (A_n(1+x)	o a_n) as (xdownarrow0). Since both (x) and (y_n(x)) tend to zero, analyticity of (R) makes
[
R(y_n(x))-R(x)	o0.
]
Therefore (7) yields
[
rac{y_n(x)}xlongrightarrow e^{a_n}.
	ag{8}
]
Because (H_n(1)=1), (8) is exactly the right derivative at the boundary, proving (1).

Since
[
a_{n+1}-a_n=rac1{p_n},
]
taking logarithms of consecutive derivatives gives (2). The marked sequence of first-order boundary dilations is therefore already faithful to the entire ordered rational-prime norm sequence.

This is a nontrivial compression of each full transition profile, but not a finite statistic for the whole prime system: recovering every prime requires the countable family ((D_n)).

## Finite-offset identity and fixed-index expansion

Subtract (7) at indices (n+1) and (n). Because
[
A_{n+1}(s)-A_n(s)=p_n^{-s},
]
one obtains the exact finite-offset relation
[
oxed{
L_n(x)
=
p_n^{-(1+x)}
+
R(y_{n+1}(x))-R(y_n(x)).
}
	ag{9}
]

For fixed (n), let
[
b_n=sum_{k<n}rac{log p_k}{p_k},
qquad
r_1=R'(0),
qquad
E_n=e^{a_n}.
]
Expanding (7) at (x=0) gives
[
y_n(x)
=
E_n x
left[
1+
igl(r_1(E_n-1)-b_nigr)x
+O_n(x^2)
ight].
	ag{10}
]
Using (9),
[
L_n(x)
=
rac1{p_n}
+
xleft[
r_1E_nigl(e^{1/p_n}-1igr)
-rac{log p_n}{p_n}
ight]
+O_n(x^2).
	ag{11}
]
The exact boundary decoder is therefore the (xdownarrow0) limit of an explicit finite-offset observable; it is not created by differentiating an unknown output calibration.

## Large-index diagonal conditioning

The useful question is whether the boundary must be approached exponentially closely as the prime index grows. Classical Mertens estimates give
[
a_n
=
loglog p_n+B_1+o(1),
	ag{12}
]
and
[
b_n
=
log p_n+O(1).
	ag{13}
]
Hence
[
E_n=e^{a_n}asymplog p_n.
	ag{14}
]

Now take any (x_n>0) with (x_nlog p_n	o0). The elementary inequality (1-e^{-u}le u) gives
[
0le
a_n-A_n(1+x_n)
le
x_n b_n
=o(1).
	ag{15}
]
Equation (7), together with (14)--(15), then implies
[
y_n(x_n)
sim
E_nx_n
asymp
x_nlog p_n
longrightarrow0.
	ag{16}
]

Next,
[
P(1+y_n)-P(1+y_{n+1})
=
p_n^{-(1+x_n)}.
	ag{17}
]
By the mean-value theorem and
[
-P'(1+u)=u^{-1}+O(1)
qquad(udownarrow0),
	ag{18}
]
equation (16) yields
[
y_{n+1}(x_n)-y_n(x_n)
=
O!left(
rac{x_nlog p_n}{p_n}
ight).
	ag{19}
]
Since (R') is bounded near zero,
[
p_nleft|
R(y_{n+1}(x_n))-R(y_n(x_n))
ight|
=
O(x_nlog p_n)
=o(1).
	ag{20}
]
Multiplying (9) by (p_n) now gives
[
p_nL_n(x_n)
=
p_n^{-x_n}+o(1)
=
e^{-x_nlog p_n}+o(1)
longrightarrow1,
]
which proves (3).

This is a source-depth statement, not a blanket noise theorem. If (L_n) is perturbed by an additive error (delta_n), the decoder (p=1/L) has local derivative of size (p_n^2). Relative prime recovery therefore requires (delta_n=o(1/p_n)), while (O(1)) absolute prime accuracy requires the stronger (delta_n=O(1/p_n^2)). The logarithmic approach scale in (3) concerns how close the exact transition must be sampled to (s=1), not how much arbitrary observation noise can be tolerated.

## Matched finite-prefix generalized-prime control

The boundary calculation is not peculiar to the exact rational-prime list. Let (q_k) be an increasing positive generator sequence that differs from (p_k) in only finitely many positions, and define
[
Q(s)=sum_kq_k^{-s},
qquad
Q_n(s)=sum_{kge n}q_k^{-s},
qquad
K_n=Q^{-1}circ Q_n.
]
The finite modification changes only the analytic regular part of the logarithmic singularity at (s=1). Repeating (7)--(8) gives
[
oxed{
K_n'(1+)
=
exp!left(sum_{k<n}rac1{q_k}ight),
}
	ag{21}
]
and therefore
[
log K_{n+1}'(1+)-log K_n'(1+)=rac1{q_n}.
	ag{22}
]

Apply this to AF-551's finite-prefix control. Its first generator is (q_1=2^c), so
[
K_2'(1+)=e^{1/q_1}=e^{2^{-c}},
]
whereas the rational-prime transition has (H_2'(1+)=e^{1/2}). The two full quotient profiles may become exponentially close on a far-right moving tail while remaining separated by a fixed first-order invariant at their common left boundary.

This is precisely the line-specific matched-control test required by the Arithmetic Fidelity mandate: the boundary carrier distinguishes the rational-prime norm from a generalized-prime deformation at an information layer where the right-tail asymptotic slope does not.

## Fidelity / representation audit

AF-550 established exact fidelity of the full nonlocal transition profile under unrestricted common output calibration. AF-551 showed that one decoder of the absolute scale—its right-tail exponentially small curvature—has exponentially collapsing horizontal separation from a matched control.

AF-552 identifies a second decoder already present in the same quotient object. It uses the source-natural singular boundary rather than the remote tail:
[
	ext{full transition profile}
longmapsto
H_n'(1+)
longmapsto
log H_{n+1}'(1+)-log H_n'(1+)
=
1/p_n.
]
The retained information is first-order at a common boundary, but it is not one of AF-548's separated finite jets. The common boundary (s=1) is in the **source coordinate**, which the target recalibration does not act on; the target nuisance has already been cancelled by forming (H_n).

The result therefore sharpens the exact-versus-stable lesson. Conditioning belongs to a representation, target, norm, and observation regime—not just to an abstract exact quotient. Exponential loss in one asymptotic channel does not certify exponential loss in every functional of the same complete quotient.

## Prior-art / novelty audit

No novelty is claimed for the underlying analytic-number-theory ingredients.

Carl-Erik Fröberg's classical prime-zeta work, already recorded under AF-017, supplies the prime-zeta/Möbius-inversion background. Artur Kawalec, *On the series expansion of the prime zeta function about s=1 and its coefficients*, arXiv:2603.21535 (2026), explicitly studies the series expansion around the logarithmic singularity; it is a recent preprint and is not treated here as peer-reviewed authority. Classical Mertens estimates supply (12)--(13).

The inverse-transition construction itself is already AF-550's quotient invariant, with relative-distribution and left-equivalence prior art recorded there. The new durable delta is the channel comparison: the exact transition identity (7) turns the logarithmic source singularity into boundary dilations whose adjacent log increments are exactly (1/p_n), and the diagonal estimate (3) shows that this carrier survives finite boundary offset on the reciprocal-logarithmic source scale.

A targeted search for prime-zeta inverse-tail transitions, (P^{-1})-based prime recovery, and boundary-derivative formulations located standard prime-zeta material but no source explicitly stating this transition-boundary decoder. Absence of a search hit is not evidence of priority, so no literature-novelty claim is made.

## Boundaries and failure modes

- **The source coordinate is retained structure.** Arbitrary reparameterization of (s) would change boundary derivatives. AF-551 likewise keeps the input coordinate rather than quotienting it.
- **The boundary is source-natural here.** For the rational prime zeta function and finite-prefix deformations, (s=1) is the common logarithmic divergence boundary. A different source need not provide the same anchor.
- **The singular coefficient matters.** Formula (21) uses that finite-prefix controls preserve the coefficient one of (-log(s-1)). A source with a different singular order requires a separately audited normal form.
- **Countably many dilations are retained.** Equation (2) does not claim finite-dimensional compression of the entire prime sequence.
- **Exact recovery is not uniform noise stability.** The adjacent signal decays like (1/p_n); noisy recovery still needs prime-dependent precision.
- **The diagonal theorem is about exact transition samples.** It does not by itself give a calibration-independent norm on noisy raw outputs before the quotient transition is formed.
- **Finite-prefix controls are only one falsification family.** Other generalized-prime deformations that alter the singular coefficient, convergence boundary, source parameterization, or infinitely many generators need separate analysis.
- **No RH consequence follows.** The full marked tail family already contains the prime data. This finding identifies a better-conditioned carrier inside that representation; it does not show that an RH-relevant downstream representation preserves it.

## Decisive audit tests

1. Starting from (P(H_n(s))=T_n(s)), substitute the boundary normal form (5) and rederive the exact equation (7).
2. Take (xdownarrow0) in (7), verify (H_n'(1+)=e^{a_n}), and check that consecutive log derivatives give exactly (1/p_n).
3. Subtract the (n) and (n+1) equations to obtain (9) without approximation, then verify the fixed-(n) expansion (11).
4. Use the two Mertens sums (12)--(13) to prove (15)--(20) and the diagonal law (p_nL_n(x_n)	o1) whenever (x_nlog p_n	o0).
5. Apply (21) to AF-551's finite-prefix power control and verify the nonzero boundary-dilation gap (e^{1/2}-e^{2^{-c}}).

## Consequence for the research line

AF-551's exponential right-tail lower bound does not extend to the whole AF-550 quotient profile. The same exact transition family has a source-boundary carrier that recovers every prime through adjacent first-order dilations and separates AF-551's matched generalized-prime control by a fixed boundary gap.

The remaining fidelity question is therefore downstream and target-specific: **does an RH-relevant representation preserve this boundary-dilation information, or an equivalent carrier, with a useful normed transport modulus?** A mechanism that discards the (s=1) boundary geometry may still inherit AF-551's exponential tail barrier; one that preserves a controlled boundary/global coupling must be audited on its own conditioning scale.
