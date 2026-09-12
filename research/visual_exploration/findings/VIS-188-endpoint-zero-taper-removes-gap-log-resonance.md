# VIS-188 — an endpoint-zero quadratic taper removes the flat gap logarithmic resonance

## Claim

Let

`w(x)=6x(1-x)`, `0<=x<=1`,

so that `w(0)=w(1)=0` and `int_0^1 w(x) dx = 1`. Replace the rectangular interval average from `VIS-185`--`VIS-187` by the normalized tapered kernel

`K^w_(H,T)(p,q)`
` = H^(-1) int_T^(T+H) w((t-T)/H) exp(it log(q/p)) dt`.

Fix `c>0`, put `H=cp`, and consider the same deterministic flat even-gap null as in `VIS-187`,

`E^w_p(M;c,T) = sum_(1<=m<=M) K^w_(cp,T)(p,p+2m)`.

Then for every `p>=2`, every real `T`, and every `1<=M<=p/2`,

`|E^w_p(M;c,T)| <= 4 pi^2/c^2`.

In particular, for every sequence `M=M(p)` with `M->infinity` and `M<=p/2`,

`E^w_p(M;c,T)/log M -> 0`

uniformly in the interval start `T`.

Thus the order-`log M` accumulation exhibited by the rectangular flat-gap null in `VIS-187` is **not an unavoidable consequence of adding many mesoscopic gap scales**. It is a hard-endpoint effect of the rectangular observation window. A simple endpoint-zero taper upgrades the kernel tail from `1/m` to `1/m^2` and removes that deterministic logarithmic resonance completely.

More generally, if `v in C^2([0,1])`, `v(0)=v(1)=0`, and `V=int_0^1 v(x) dx != 0`, then the normalized `v`-tapered kernel satisfies

`|K^v_(H,T)(p,q)| <= C_v/(H |log(q/p)|)^2`,

where

`C_v = (|v'(0)|+|v'(1)|+int_0^1 |v''(x)| dx)/|V|`.

The quadratic taper is the explicit specialization `C_w=24`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FOURIER-WINDOW MECHANISM + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No statement is made here about the complete prime-pair off-diagonal sum, optimal tapers, or a new theorem in Fourier/window analysis.

## 1. The tapered kernel is a Fourier transform of the window

Write

`u=log(q/p)`.

With the change of variables `t=T+Hx`,

`K^w_(H,T)(p,q)`
` = exp(iTu) int_0^1 w(x) exp(i H u x) dx`.

Hence the interval start contributes only a unimodular phase. All decay is controlled by the Fourier transform of the compactly supported taper.

For a general `v` as in the claim, put `z=Hu`. Two integrations by parts give

`int_0^1 v(x) exp(i z x) dx`
` = -[v'(1) exp(i z)-v'(0)]/(i z)^2`
`   + (1/(i z)^2) int_0^1 v''(x) exp(i z x) dx`.

The first integration has no boundary term because `v(0)=v(1)=0`. Therefore

`|int_0^1 v(x) exp(i z x) dx|`
` <= [|v'(0)|+|v'(1)|+int_0^1 |v''(x)| dx]/|z|^2`.

After division by `|V|` for a general normalized taper, this is the stated `C_v/|z|^2` bound.

For `w(x)=6x(1-x)`,

`w'(0)=6`, `w'(1)=-6`, `w''(x)=-12`,

so

`C_w = 6+6+12 = 24`.

Thus

`|K^w_(H,T)(p,q)| <= 24/(H |log(q/p)|)^2`.

## 2. Flat even gaps become absolutely summable

Take `q=p+2m`, `H=cp`, and `1<=m<=p/2`. Since `0<=2m/p<=1`,

`log(1+2m/p) >= (2m/p)/(1+2m/p) >= m/p`.

Consequently

`H log((p+2m)/p) >= c m`,

and therefore

`|K^w_(cp,T)(p,p+2m)| <= 24/(c^2 m^2)`.

Summing absolutely,

`|E^w_p(M;c,T)|`
` <= (24/c^2) sum_(m<=M) 1/m^2`
` <= (24/c^2) * pi^2/6`
` = 4 pi^2/c^2`.

The bound is independent of `T`, `p`, and `M` in the stated range. Dividing by `log M` proves the uniform vanishing assertion whenever `M->infinity`.

The contrast with `VIS-187` is exact at the level of Fourier tails. The rectangular window has a jump at each endpoint, so its transform has a leading `1/z` boundary term. On the linear gap scale `z asymp m`, summing this tail produces a harmonic series and permits the endpoint-resonant `log M` term. Making the window itself vanish at both endpoints removes that first boundary term; the remaining `1/z^2` tail is summable.

## 3. This isolates the source of the previous resonance

`VIS-185` used the exact rectangular interval kernel to improve a crude modulus-one bound. `VIS-186` then showed that each fixed polynomial gap shell is negligible, while leaving open coherent accumulation across `Theta(log y)` shells. `VIS-187` supplied a decisive deterministic null: with a hard rectangular window, a flat even-gap profile can indeed accumulate logarithmically when one scaled endpoint is resonant.

The present result separates **cross-scale crowding** from **hard-window endpoint leakage**. The flat gap model still contains all scales `1<=m<=M`, but once the observation window is tapered to zero at both ends, the logarithmic floor disappears uniformly in the start phase. Thus a future arithmetic cross-scale statistic need not inherit the rectangular endpoint obstruction if its observation functional is chosen with sufficient endpoint regularity.

This does not prove that a tapered prime-pair statistic is small. Prime multiplicities, singular-series weights, the full `p^(-alpha)(p+d)^(-alpha)` profile, variation across dyadic prime blocks, and genuinely macroscopic separations remain separate issues. What is removed here is one specific deterministic false positive.

## 4. Prior-art and novelty boundary

The underlying Fourier principle is classical windowing/apodization: tapering a finite observation interval suppresses spectral leakage, and smoother endpoint behavior produces faster transform decay. Fredric J. Harris, **On the use of windows for harmonic analysis with the discrete Fourier transform**, *Proceedings of the IEEE* 66:1 (1978), 51--83, DOI `10.1109/PROC.1978.10837`, is a standard survey of this windowing tradeoff and catalogs classical tapered windows.

No novelty is claimed for the fact that endpoint-zero windows have better Fourier tails, for the quadratic/parabolic taper, or for the two integrations by parts above. The Mathia-specific content is the placement of that classical mechanism against `VIS-187`: it proves that the deterministic `log M` gap accumulation identified there is removable by a source-independent change of observation window, so it must not be treated as an intrinsic multiscale arithmetic signal.

## 5. Boundaries and falsification

The explicit flat-gap bound uses `M<=p/2` only to obtain the simple uniform inequality

`p log(1+2m/p) >= m`.

The conclusion is therefore already strong enough for every sublinear and every fixed polynomial cumulative gap range below the linear scale. No claim is made here for `m` much larger than `p`, where the frequency geometry changes.

The taper is fixed as `p` grows and is normalized to unit mass. A family of increasingly sharp tapers could reintroduce large derivative constants and would require a separate uniform analysis.

The result removes the rectangular endpoint-resonance null, not all deterministic controls. A tapered statistic may still exhibit structure caused by the taper's own transfer function, by coarse gap density, by weighting, or by another representation artifact. Those must be matched separately before an arithmetic interpretation.

Falsify the finding by locating an error in the change of variables, either integration by parts, the constant `C_w=24`, the lower bound for `p log(1+2m/p)`, or the absolute `m^(-2)` summation.

## Research consequence

For the live multiscale gap frontier, a **smooth-window comparison is now mandatory before attributing logarithmic cross-shell accumulation to arithmetic structure**. The rectangular and endpoint-zero tapered statistics form a useful matched pair: a signal that disappears under tapering is compatible with hard-endpoint leakage, while a residual that survives with a quantitatively controlled taper has passed one stronger representation-artifact test.

The next independent question is whether the actual full-prefix prime-pair off-diagonal contribution, with its arithmetic weights and singular-series structure, remains negligible under such a taper across cumulative polynomial gap ranges. That is a new theorem surface rather than a prerequisite for the present negative control.